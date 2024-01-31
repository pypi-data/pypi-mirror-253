"""
Make the update of protected tag.
"""

# Standard Library
from typing import List  # pylint: disable=unused-import

# Third Party Libraries
import attr
import click

from gitlab.const import MAINTAINER_ACCESS

# Gitlab-Project-Configurator Modules
from gpc.change_setting import ChangePropertySetting
from gpc.executors.properties_updator import ChangePropertyExecutor
from gpc.helpers.gitlab_helper import MAP_ACCESS_REVERT
from gpc.parameters import RunMode
from gpc.property_manager import PropertyBean
from gpc.property_manager import PropertyManager


@attr.s(eq=False)
class ProtectedTag(PropertyBean):
    allowed_to_create = attr.ib()  # type: List

    @staticmethod
    def to_protected_tags(api_protected_tags):
        protected_tags = []  # type: List[ProtectedTag]
        for api_protected_tag in api_protected_tags:
            protected_tags.append(ProtectedTag.to_protected_tag(api_protected_tag))
        return protected_tags

    @staticmethod
    def to_protected_tag(api_protected_tag):
        allowed_to_create = []
        for create_access in api_protected_tag.create_access_levels:
            allowed_to_create.append(create_access.get("access_level"))

        return ProtectedTag(name=api_protected_tag.name, allowed_to_create=allowed_to_create)

    def get_query(self):
        if len(self.allowed_to_create) != 1:
            click.secho(
                "The API supports only one access role to protected tags,"
                f" so the value applied is maintainers for {self.name}"
            )
            create_access_level = MAINTAINER_ACCESS
        else:
            create_access_level = self.allowed_to_create[0]
        return {"name": self.name, "create_access_level": create_access_level}

    def to_dict(self):
        allowed_to_create = sorted(MAP_ACCESS_REVERT.get(x) for x in self.allowed_to_create)
        return {"name": self.name, "allowed_to_create": allowed_to_create}

    def __eq__(self, other):
        if not isinstance(other, ProtectedTag):
            return False
        return self.name == other.name and sorted(self.allowed_to_create) == sorted(
            other.allowed_to_create
        )


class ChangeProtectedTag(ChangePropertySetting):
    sub_properties = ["allowed_to_create"]
    status_to_process = ["removed", "updated", "kept", "added"]


class ProtectedTagSettingExecutor(ChangePropertyExecutor):
    order = 30
    name = "protected_tags"
    sections = ["protected_tags"]

    def _apply(self):
        if self.changes:
            change_protected_tags = self.changes[0]
            self._save_properties(
                PropertyManager(self.project.protectedtags),
                change_protected_tags,
                change_protected_tags.after,
            )

    def _update(self, mode: RunMode, members_user, members_group):
        if "protected_tags" in self.rule and self.rule.protected_tags is not None:
            protected_tags = []
            keep_existing_tags = self.rule.get("keep_existing_protected_tags", False)
            for protected_tag in self.rule.protected_tags:
                protected_tags.append(
                    ProtectedTag(
                        protected_tag.pattern,
                        [self._get_role_id(protected_tag.allowed_to_create)],
                    )
                )
            self.changes.append(
                ChangeProtectedTag(
                    property_name="protected_tags",
                    before=ProtectedTag.to_protected_tags(
                        self.project.protectedtags.list(  # type: ignore
                            as_list=False, retry_transient_errors=True
                        )
                    ),
                    after=protected_tags,
                    show_diff_only=self.show_diff_only,
                    keep_existing=keep_existing_tags,
                )
            )
