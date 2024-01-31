"""
Executor to manage the members of a project.
"""

# Standard Library
from typing import List  # pylint: disable=unused-import

# Third Party Libraries
import attr
import gitlab

from boltons.cacheutils import cachedproperty
from structlog import get_logger

# Gitlab-Project-Configurator Modules
from gpc.change_setting import ChangePropertySetting
from gpc.executors.profile_member_mixin import GPCUser
from gpc.executors.profile_member_mixin import ProfileMemberMixin
from gpc.executors.properties_updator import ChangePropertyExecutor
from gpc.helpers.exceptions import GpcMemberError
from gpc.helpers.gitlab_helper import MAP_ACCESS
from gpc.helpers.gitlab_helper import MAP_ACCESS_REVERT
from gpc.parameters import RunMode
from gpc.property_manager import PropertyBean


log = get_logger()

GROUP = "group"
USER = "user"


@attr.s
class ProjectMember(PropertyBean):
    role = attr.ib()  # type: int
    member_type = attr.ib()  # type: str
    member_id = attr.ib()  # type: int

    @property
    def role_name(self):
        return MAP_ACCESS_REVERT[self.role]

    def get_query(self):
        pass

    def to_dict(self):
        return {"name": self.name, "role": self.role_name}


class ChangeProjectMembers(ChangePropertySetting):
    sub_properties = ["role"]  # type: List[str]
    status_to_process = ["removed", "updated", "kept", "added", "error"]

    @cachedproperty
    def action(self):
        if {m["status"] for m in self.differences.values()} == {"kept"}:
            return "kept"
        if self.after and self.before is None:
            return "added"
        if self.after is None and self.before:
            return "removed"
        return "updated"

    def rich_rows(self, console):
        table_rows = []
        table_rows.append(
            (
                (
                    self.wrap_text(self.property_name, console, "property_name"),
                    "",
                    "",
                    "",
                ),
                self.get_line_color(self.action),
            )
        )
        for changes in self.differences.values():
            line_color = self.get_line_color(changes["status"])
            name_before = changes["before"]["name"] if changes["before"] else ""
            name_after = changes["after"]["name"] if changes["after"] else ""
            role_before = changes["before"]["role"] if changes["before"] else ""
            role_after = changes["after"]["role"] if changes["after"] else ""
            status = changes["status"]

            table_rows.append(
                (
                    (
                        self.wrap_text("name", console, "property_name"),
                        self.wrap_text(
                            name_before,
                            console,
                            "before",
                        ),
                        self.wrap_text(
                            name_after,
                            console,
                            "after",
                        ),
                        "",
                    ),
                    line_color,
                )
            )
            table_rows.append(
                (
                    (
                        self.wrap_text("role", console, "property_name"),
                        self.wrap_text(
                            role_before,
                            console,
                            "before",
                        ),
                        self.wrap_text(
                            role_after,
                            console,
                            "after",
                        ),
                        status,
                    ),
                    line_color,
                )
            )
            table_rows.append("new_line")

        table_rows.append("new_section")
        return table_rows


class MembersProjectExecutor(ChangePropertyExecutor, ProfileMemberMixin):
    # Last section displayed
    order = 11
    applicable_to = ["group", "project"]
    sections = ["members"]
    name = "members"

    @cachedproperty
    def inherited_members(self):
        members = {}
        # We kept members_all api here even though it is not always
        # accurate because users api does not return  access level
        for user in self.project.members_all.list(
            as_list=True, all=True, retry_transient_errors=True
        ):
            members[user.username] = ProjectMember(
                name=user.username,
                member_id=user.id,
                member_type=USER,
                role=user.access_level,
            )
        return members

    def _apply(self):
        members_error = []
        if self.changes:
            members = self.changes[0]
            if members.has_diff():
                before = {prop.name: prop for prop in members.before}
                after = {prop.name: prop for prop in members.after}
                for member, diff in members.differences.items():
                    try:
                        status = diff["status"]
                        match status:
                            case "added":
                                self._create_member(after, member)
                            case "updated":
                                self._update_member(after, member)
                            case "removed":
                                self._rm_member(before, member)

                    except Exception as e:
                        diff["status"] = "error"
                        log.error(
                            f"An error occurred with member '{member}' on {self.project_path}",
                            error_message=str(e),
                        )
                        members_error.append(member)
        if members_error:
            raise GpcMemberError(f"An error with the following members: {members_error}")

    def _create_member(self, dict_project_members, member_name):
        pm = dict_project_members[member_name]
        if pm.member_type == USER:
            self.project.members.create(
                {"user_id": pm.member_id, "access_level": pm.role}, retry_transient_errors=True
            )
        else:
            self.project.share(pm.member_id, pm.role, retry_transient_errors=True)

    def _update_member(self, dict_project_members, member_name):
        pm = dict_project_members[member_name]
        if pm.member_type == GROUP:
            self.project.unshare(pm.member_id, retry_transient_errors=True)
            self.project.share(pm.member_id, pm.role, retry_transient_errors=True)
        else:
            member = self.project.members.get(pm.member_id, retry_transient_errors=True)
            member.access_level = pm.role
            member.save(retry_transient_errors=True)

    def _rm_member(self, dict_project_members, member_name):
        pm = dict_project_members[member_name]
        if pm.member_type == GROUP:
            self.project.unshare(pm.member_id, retry_transient_errors=True)
        else:
            self.project.members.delete(pm.member_id, retry_transient_errors=True)

    def _update(self, mode: RunMode, members_user, members_group):
        if (
            self.rule.get("project_members") is not None
            or self.rule.get("group_members") is not None
        ):
            project_members = self.get_project_members_to_update(members_user, members_group)
            keep_existing_members = self.rule.get("keep_existing_members", False)

            old_project_members = self.get_current_members()
            skip_members = self._check_members(old_project_members, project_members)
            self.changes.append(
                ChangeProjectMembers(
                    "members",
                    list(old_project_members.values()),
                    list(project_members.values()),
                    self.show_diff_only,
                    keep_existing=keep_existing_members,
                )
            )
            for member in skip_members:
                self.changes[0].differences[member]["status"] = "kept"  # type: ignore

    def _check_members(self, old_project_members, project_members):
        members_error = []
        skip_members = []
        for member_name in project_members:
            if member_name not in old_project_members and member_name in self.inherited_members:
                # Check if member is not inherited from parents groups.
                inherited_member = self.inherited_members[member_name]
                if self.rule.get("skip_permission_error", False):
                    if inherited_member.role > project_members[member_name].role:
                        log.info(
                            f"skip_permission_error enabled: {member_name} has"
                            f" already '{MAP_ACCESS_REVERT[inherited_member.role]}' rights on"
                            f" the project {self.project_path}, skipping..."
                        )
                        skip_members.append(member_name)

                elif inherited_member.role == gitlab.OWNER_ACCESS:
                    # If the member is inherited and has higher right, we prevent
                    # an error from the API.
                    members_error.append(member_name)
        if members_error:
            raise GpcMemberError(
                f"The users '{members_error}' can not be add to"
                f" the project {self.project_path} because "
                "they are inherited members "
                "with owner access."
            )
        return skip_members

    def get_project_members_to_update(self, members_user, members_group):
        project_members_settings = (
            self.rule.get("project_members")
            if self.rule.get("project_members")
            else self.rule.get("group_members")
        )
        project_members = {}
        if "profiles" in project_members_settings:
            for profile_name in project_members_settings.profiles:
                profile = self.get_member_profile(profile_name)
                if "role" not in profile:
                    raise GpcMemberError(
                        "The role is missing in your "
                        f"member_profiles definition '{profile_name}'."
                    )
                for member in profile.members:
                    project_members[member] = self._init_project_member(
                        member, profile.role, members_user, members_group
                    )
        if "members" in project_members_settings:
            project_members.update(
                self._extract_members(members_group, members_user, project_members_settings.members)
            )
        return project_members

    def _extract_members(self, members_group, members_user, members):
        project_members = {}
        for member in members:
            if "names" in member:
                for name in member.names:
                    project_members[name] = self._init_project_member(
                        name, member.role, members_user, members_group
                    )
            if "name" in member:
                project_members[member.name] = self._init_project_member(
                    member.name, member.role, members_user, members_group
                )
        return project_members

    def _init_project_member(self, member_name, role, members_user, members_group):
        member = self.get_member(member_name)
        if isinstance(member, GPCUser):
            members_user.append(member.gl_id)
            return ProjectMember(
                name=member.name,
                role=MAP_ACCESS.get(role),
                member_id=member.gl_id,
                member_type=USER,
            )
        # GPCGroup
        members_group.append(member.full_path)
        return ProjectMember(
            name=member.full_path,
            role=MAP_ACCESS.get(role),
            member_id=member.gl_id,
            member_type=GROUP,
        )

    def get_current_members(self):
        current_members = {}
        for user in self.project.members.list(as_list=False, retry_transient_errors=True):
            current_members[user.username] = ProjectMember(
                name=user.username,
                member_type=USER,
                member_id=user.id,
                role=user.access_level,
            )
        for group in self.project.shared_with_groups:
            current_members[group["group_full_path"]] = ProjectMember(
                name=group["group_full_path"],
                member_type=GROUP,
                member_id=group["group_id"],
                role=group["group_access_level"],
            )
        return current_members
