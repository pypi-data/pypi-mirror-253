"""
Make the update of default branch, visibility, merge method and merge restriction.
"""

# Standard Library
from abc import abstractmethod
from textwrap import indent
from typing import List
from typing import Optional

# Third Party Libraries
import attr
import click

from boltons.cacheutils import cachedproperty
from gitlab.exceptions import GitlabGetError
from gitlab.exceptions import GitlabUpdateError
from gitlab.v4.objects import ProjectManager

# Gitlab-Project-Configurator Modules
from gpc.change_setting import ChangeSetting
from gpc.executors.change_executor import ChangeExecutor
from gpc.helpers.exceptions import GpcError
from gpc.helpers.exceptions import GpcPermissionError
from gpc.helpers.gitlab_helper import INV_SQUASH_OPTIONS
from gpc.helpers.gitlab_helper import MERGE_METHODS
from gpc.helpers.gitlab_helper import SQUASH_OPTIONS
from gpc.helpers.gitlab_helper import VISIBILITY_VALUES
from gpc.helpers.graphql_helper import GraphqlSingleton
from gpc.helpers.types import ProjectRule
from gpc.parameters import GpcParameters
from gpc.parameters import RunMode


class ProjectSettingExecutor(ChangeExecutor):
    order = 10
    name = "project_members"
    sections = ["default_branch", "permissions", "mergerequests"]
    project_properties = [
        "default_branch",
        "description",
        "topics",
        "ci_config_path",
        "ci_git_shallow_clone",
        "auto_cancel_pending_pipelines",
        "build_coverage_regex",
        "squash_commit_template",
        "merge_commit_template",
        "merge_requests_template",
    ]

    @cachedproperty
    def updators(self):
        return UpdatorFactory.init_updators(
            self.project, self.rule, self.show_diff_only, self.gpc_params
        )

    @cachedproperty
    def default_branch_updator(self):
        for updator in self.updators:
            if isinstance(updator, DefaultBranchUpdator):
                return updator
        return None

    def _apply(self):
        if not self.default_branch_updator.success:
            click.secho(
                "ERROR: The default branch can not be updated because an error "
                f"occurred previously: {self.default_branch_updator.error}",
                fg="red",
            )
            self.success = False
        if self.changes:
            try:
                self.project.save(retry_transient_errors=True)
            except GitlabUpdateError as e:
                if e.response_code == 403:
                    error_message = (
                        f"On project {self.project_path}: Access forbidden.\n"
                        "To update the permission, your Gitlab token should"
                        " be administrator of the project."
                    )
                    raise GpcPermissionError(error_message) from e
                raise

    def _update(self, mode: RunMode, members_user, members_group):
        """Update settings project."""
        for updator in self.updators:
            change_setting = updator.update()
            if updator.error:
                self.warnings.append(updator.error)
            if change_setting:
                self.changes.append(change_setting)


class UpdatorFactory:
    @staticmethod
    def init_updators(
        project: ProjectManager, rule: ProjectRule, show_diff_only: bool, gpc_params: GpcParameters
    ):
        updators = [
            DefaultBranchUpdator(project, rule, show_diff_only),
            DescriptionUpdator(project, rule, show_diff_only),
            TopicsUpdator(project, rule, show_diff_only),
            CiConfigPathUpdator(project, rule, show_diff_only),
            AutoCancelPendingPipelinesUpdator(project, rule, show_diff_only),
            MergeCommitTemplateUpdator(project, rule, show_diff_only),
            SquashCommitTemplateUpdator(project, rule, show_diff_only),
            IssuesTemplateUpdator(project, rule, show_diff_only),
            BuildCoverageRegexUpdator(project, rule, show_diff_only),
            CIGitShallowCloneUpdator(project, rule, show_diff_only),
            GroupUpdator(
                "artifacts",
                [
                    KeepLatestArtifactUpdator,
                ],
                project,
                rule,
                show_diff_only,
            ),
            GroupUpdator(
                "permissions",
                [
                    VisibilityUpdator,
                    RequestAccessUpdator,
                    WikiEnabledUpdator,
                    IssuesEnabledUpdator,
                    SnippetsEnabledUpdator,
                    LfsEnabledUpdator,
                    ContainerRegistryEnabledUpdator,
                    JobsEnabledUpdator,
                    MergeRequestsEnabledUpdator,
                    PackagesEnabled,
                    ReleasesAccessLevelUpdator,
                    InfrastructureAccessLevelUpdator,
                    FeatureFlagsAccessLevelUpdator,
                    EnvironmentsAccessLevelUpdator,
                    MonitorAccessLevelUpdator,
                    PagesAccessLevelUpdator,
                    AnalyticsAccessLevelUpdator,
                    ForkingAccessLevelUpdator,
                    SecurityAndComplianceAccessLevelUpdator,
                ],
                project,
                rule,
                show_diff_only,
            ),
            GroupUpdator(
                "mergerequests",
                [
                    MergeDiscussionResolvedUpdator,
                    MergePipelineSuccessUpdator,
                    ResolveOutdatedDiscussionsUpdator,
                    PrintMRLinkUpdator,
                    RemoveSourceBranchUpdator,
                    MergeMethodUpdator,
                    SquashOptionUpdator,
                    ResultPipelineUpdator,
                    MergeTrainUpdator,
                    MergeRequestsTemplateUpdator,
                    TokenAccessUpdator,
                ],
                project,
                rule,
                show_diff_only,
            ),
            GroupUpdator(
                "access_token",
                [Allow_Token_Ci_Updator, AllowList, Limit_Token_Ci_Updator, LimitList],
                project,
                rule,
                show_diff_only,
                params=gpc_params,
            ),
        ]
        return updators


@attr.s
class GroupSetting(ChangeSetting):
    change_settings = attr.ib(default=None)  # type: List[ChangeSetting]

    def to_dict(self):
        before = {}
        after = {}
        differences = {"before": before, "after": after, "action": self.action}
        result = {"property_name": self.property_name, "differences": differences}
        for change_setting in self.change_settings:
            before[change_setting.property_name] = change_setting.before
            after[change_setting.property_name] = change_setting.after
        return result

    def rich_rows(self, console):
        table_rows = []
        table_rows.append(
            (
                (
                    self.wrap_text(self.property_name, console, "property_name"),
                    "",
                    "",
                    self.action,
                ),
                self.get_line_color(self.action),
            )
        )
        for k, _ in enumerate(self.change_settings):
            table_rows.append(
                (
                    (
                        self.wrap_text(
                            self.change_settings[k].property_name, console, "property_name"
                        ),
                        self.wrap_text(str(self.change_settings[k].before), console, "before"),
                        self.wrap_text(str(self.change_settings[k].after), console, "after"),
                        self.change_settings[k].action,
                    ),
                    self.get_line_color(self.change_settings[k].action),
                )
            )
        table_rows.append("new_section")
        return table_rows

    @cachedproperty
    def action(self):
        for change_setting in self.change_settings:
            if change_setting.action != "kept":
                return "updated"
        return "kept"


class LocalUpdator:
    def __init__(
        self,
        project: ProjectManager,
        rule: ProjectRule,
        show_diff_only: bool,
        sub_level: int = 0,
        params: Optional[GpcParameters] = None,
    ):
        self.project = project
        self.rule = rule
        self.show_diff_only = show_diff_only
        self.sub_level = sub_level
        self.success = True
        self.error = ""
        self.params = params

    @abstractmethod
    def update(self):
        raise NotImplementedError()


class GroupUpdator(LocalUpdator):
    def __init__(
        self,
        property_name: str,
        group_setting_updators: List,
        project: ProjectManager,
        rule: ProjectRule,
        show_diff_only: bool,
        sub_level: int = 0,
        params: Optional[GpcParameters] = None,
    ):
        super().__init__(project, rule, show_diff_only, sub_level)
        self.property_name = property_name
        self.group_setting_updators = group_setting_updators
        self.params = params

    def update(self):
        change_settings = []
        for updator_class in self.group_setting_updators:
            updator = updator_class(
                project=self.project,
                rule=self.rule,
                show_diff_only=self.show_diff_only,
                sub_level=1,
                params=self.params,
            )
            change_setting = updator.update()
            if change_setting:
                change_settings.append(change_setting)
        if change_settings:
            return GroupSetting(
                property_name=self.property_name,
                before=None,
                after=None,
                show_diff_only=self.show_diff_only,
                change_settings=change_settings,
            )
        return None


class DefaultBranchUpdator(LocalUpdator):
    def update(self):
        if "default_branch" in self.rule and self.rule.default_branch:
            force_create_default_branch = (
                "force_create_default_branch" in self.rule and self.rule.force_create_default_branch
            )
            branch_treatment = (
                self.create_default_branch if force_create_default_branch else self.exist_branch
            )
            if branch_treatment(self.rule.default_branch):
                change_setting = ChangeSetting(
                    property_name="default_branch",
                    before=self.project.default_branch,
                    after=self.rule.default_branch,
                    show_diff_only=self.show_diff_only,
                )
                self.project.default_branch = self.rule.default_branch
            else:
                change_setting = ChangeSetting(
                    property_name="default_branch",
                    before=self.project.default_branch,
                    after=f"{self.rule.default_branch} (does not exist)",
                    show_diff_only=self.show_diff_only,
                )
                change_setting.action = "error"
            return change_setting
        return None

    def create_default_branch(self, branch_name):
        try:
            self.project.branches.get(branch_name, retry_transient_errors=True)
            return True
        except GitlabGetError as exc:
            if exc.response_code == 404:
                # if the branch does not exist we create it
                self.project.branches.create(
                    {"branch": branch_name, "ref": self.project.default_branch},
                    retry_transient_errors=True,
                )
                return True

            raise

    def exist_branch(self, branch_name):
        try:
            self.project.branches.get(branch_name, retry_transient_errors=True)
            return True
        except GitlabGetError as exc:
            if exc.response_code in (404, 500):
                # Gitlab.org may return error 500 for projects that does not have
                # any branch
                self.success = False
                self.error = (
                    f"The branch {branch_name} does not exist for"
                    f" the project {self.project.path_with_namespace}."
                )
                click.secho(
                    f"/!\\ {self.error} The default branch will not be updated."
                    "You may try with force_create_default_branch option to force its creation.",
                    fg="yellow",
                )
                return False
            raise


class ArtifactsUpdator(LocalUpdator):
    artifact_param_name = None  # type: str

    def update(self):
        if "artifacts" in self.rule and self.artifact_param_name in self.rule.artifacts:
            self.filter_value(getattr(self.rule.artifacts, self.artifact_param_name))
            change_setting = ChangeSetting(
                property_name=self.artifact_param_name,
                before=getattr(self.project, self.artifact_param_name),
                after=getattr(self.rule.artifacts, self.artifact_param_name),
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            setattr(
                self.project,
                self.artifact_param_name,
                getattr(self.rule.artifacts, self.artifact_param_name),
            )
            return change_setting
        return None

    def filter_value(self, _value):
        pass


class KeepLatestArtifactUpdator(ArtifactsUpdator):
    artifact_param_name = "keep_latest_artifact"


class DescriptionUpdator(LocalUpdator):
    def update(self):
        if "description" in self.rule:
            change_setting = ChangeSetting(
                property_name="description",
                before=self.project.description,
                after=self.rule.description,
                show_diff_only=self.show_diff_only,
            )
            self.project.description = self.rule.description
            return change_setting
        return None


class TopicsUpdator(LocalUpdator):
    def update(self):
        if "topics" in self.rule and isinstance(self.rule.topics, list):
            if self.rule.get("keep_existing_topics", False):
                for topic in self.project.topics:
                    if topic not in self.rule.topics:
                        self.rule.topics.append(topic)
            change_setting = ChangeSetting(
                property_name="topics",
                before=self.project.topics,
                after=self.rule.topics,
                show_diff_only=self.show_diff_only,
            )
            self.project.topics = self.rule.topics
            return change_setting
        return None


class CiConfigPathUpdator(LocalUpdator):
    def update(self):
        if "ci_config_path" in self.rule:
            change_setting = ChangeSetting(
                property_name="ci_config_path",
                before=self.project.ci_config_path,
                after=self.rule.ci_config_path,
                show_diff_only=self.show_diff_only,
            )
            self.project.ci_config_path = self.rule.ci_config_path
            return change_setting
        return None


class AutoCancelPendingPipelinesUpdator(LocalUpdator):
    def update(self):
        if "auto_cancel_pending_pipelines" in self.rule:
            change_setting = ChangeSetting(
                property_name="auto_cancel_pending_pipelines",
                before=self.project.auto_cancel_pending_pipelines,
                after=self.rule.auto_cancel_pending_pipelines,
                show_diff_only=self.show_diff_only,
            )
            self.project.auto_cancel_pending_pipelines = self.rule.auto_cancel_pending_pipelines
            return change_setting
        return None


class MergeCommitTemplateUpdator(LocalUpdator):
    def update(self):
        if "merge_commit_template" in self.rule:
            change_setting = ChangeSetting(
                property_name="merge_commit_template",
                before=self.project.merge_commit_template,
                after=self.rule.merge_commit_template,
                show_diff_only=self.show_diff_only,
            )
            self.project.merge_commit_template = self.rule.merge_commit_template
            return change_setting
        return None


class SquashCommitTemplateUpdator(LocalUpdator):
    def update(self):
        if "squash_commit_template" in self.rule:
            change_setting = ChangeSetting(
                property_name="squash_commit_template",
                before=self.project.squash_commit_template,
                after=self.rule.squash_commit_template,
                show_diff_only=self.show_diff_only,
            )
            self.project.squash_commit_template = self.rule.squash_commit_template
            return change_setting
        return None


class IssuesTemplateUpdator(LocalUpdator):
    def update(self):
        if "issues_template" in self.rule:
            change_setting = ChangeSetting(
                property_name="issues_template",
                before=self.project.issues_template,
                after=self.rule.issues_template,
                show_diff_only=self.show_diff_only,
            )
            self.project.issues_template = self.rule.issues_template
            return change_setting
        return None


class MergeRequestsTemplateUpdator(LocalUpdator):
    def update(self):
        if "mergerequests" in self.rule and "default_template" in self.rule.mergerequests:
            change_setting = ChangeSetting(
                property_name="merge_requests_template",
                before=self.project.merge_requests_template,
                after=self.rule.mergerequests.default_template,
                show_diff_only=self.show_diff_only,
            )
            self.project.merge_requests_template = self.rule.mergerequests.default_template
            return change_setting
        return None


class BuildCoverageRegexUpdator(LocalUpdator):
    def update(self):
        if "build_coverage_regex" in self.rule:
            self.error = "build_coverage_regex deprecated in Gitlab 15.0"


class CIGitShallowCloneUpdator(LocalUpdator):
    def update(self):
        if "ci_git_shallow_clone" in self.rule:
            p_ci_git_shallow_clone = self.project.ci_default_git_depth
            # 0 or None are the same value for gitlab
            if not self.project.ci_default_git_depth:
                p_ci_git_shallow_clone = None
            r_ci_git_shallow_clone = self.rule.ci_git_shallow_clone
            # 0 or None are the same value for gitlab
            if not self.rule.ci_git_shallow_clone:
                r_ci_git_shallow_clone = None
            change_setting = ChangeSetting(
                property_name="ci_git_shallow_clone",
                before=p_ci_git_shallow_clone,
                after=r_ci_git_shallow_clone,
                show_diff_only=self.show_diff_only,
            )
            self.project.ci_default_git_depth = self.rule.ci_git_shallow_clone
            return change_setting
        return None


class PermissionsUpdator(LocalUpdator):
    permission_rule_name = None  # type: str

    def update(self):
        if "permissions" in self.rule and self.permission_rule_name in self.rule.permissions:
            self.filter_value(getattr(self.rule.permissions, self.permission_rule_name))
            change_setting = ChangeSetting(
                property_name=self.permission_rule_name,
                before=getattr(self.project, self.permission_rule_name),
                after=getattr(self.rule.permissions, self.permission_rule_name),
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            setattr(
                self.project,
                self.permission_rule_name,
                getattr(self.rule.permissions, self.permission_rule_name),
            )
            return change_setting
        return None

    def filter_value(self, _value):
        pass


class VisibilityUpdator(PermissionsUpdator):
    permission_rule_name = "visibility"

    def filter_value(self, value):
        if value not in VISIBILITY_VALUES:
            raise ValueError(
                f"the visibility value '{value}' is not acceptable, "
                f"the value should be in : {VISIBILITY_VALUES}."
            )

    def update(self):
        if "permissions" in self.rule and self.permission_rule_name in self.rule.permissions:
            self.filter_value(getattr(self.rule.permissions, self.permission_rule_name))
            change_setting = ChangeSetting(
                property_name=self.permission_rule_name,
                before=getattr(self.project, self.permission_rule_name),
                after=getattr(self.rule.permissions, self.permission_rule_name),
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            if (
                change_setting.before in ["internal", "private"]
                and change_setting.after == "public"
            ):
                change_setting.action = "error"
                click.secho(
                    "Access forbidden."
                    " To update the permission on this project, your Gitlab token should"
                    " be administrator of the project.",
                    fg="red",
                )
            setattr(
                self.project,
                self.permission_rule_name,
                getattr(self.rule.permissions, self.permission_rule_name),
            )
            return change_setting
        return None


class RequestAccessUpdator(PermissionsUpdator):
    permission_rule_name = "request_access_enabled"


class WikiEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "wiki_enabled"


class IssuesEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "issues_enabled"


class SnippetsEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "snippets_enabled"


class LfsEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "lfs_enabled"


class ContainerRegistryEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "container_registry_enabled"


class ReleasesAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "releases_access_level"


class InfrastructureAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "infrastructure_access_level"


class FeatureFlagsAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "feature_flags_access_level"


class EnvironmentsAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "environments_access_level"


class MonitorAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "monitor_access_level"


class PagesAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "pages_access_level"


class AnalyticsAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "analytics_access_level"


class ForkingAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "forking_access_level"


class SecurityAndComplianceAccessLevelUpdator(PermissionsUpdator):
    permission_rule_name = "security_and_compliance_access_level"


class JobsEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "jobs_enabled"


class MergeRequestsEnabledUpdator(PermissionsUpdator):
    permission_rule_name = "merge_requests_enabled"


class PackagesEnabled(PermissionsUpdator):
    permission_rule_name = "packages_enabled"


class MergeDiscussionResolvedUpdator(LocalUpdator):
    def update(self):
        if (
            "mergerequests" in self.rule
            and "only_allow_merge_if_all_discussions_are_resolved" in self.rule.mergerequests
        ):
            mr_config = self.rule.mergerequests
            change_setting = ChangeSetting(
                property_name="only_allow_merge_if_all_discussions_are_resolved",
                before=self.project.only_allow_merge_if_all_discussions_are_resolved,
                after=mr_config.only_allow_merge_if_all_discussions_are_resolved,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.only_allow_merge_if_all_discussions_are_resolved = (
                mr_config.only_allow_merge_if_all_discussions_are_resolved
            )
            return change_setting
        return None


class MergePipelineSuccessUpdator(LocalUpdator):
    def update(self):
        if (
            "mergerequests" in self.rule
            and "only_allow_merge_if_pipeline_succeeds" in self.rule.mergerequests
        ):
            mr_config = self.rule.mergerequests
            change_setting = ChangeSetting(
                property_name="only_allow_merge_if_pipeline_succeeds",
                before=self.project.only_allow_merge_if_pipeline_succeeds,
                after=mr_config.only_allow_merge_if_pipeline_succeeds,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.only_allow_merge_if_pipeline_succeeds = (
                mr_config.only_allow_merge_if_pipeline_succeeds
            )
            return change_setting
        return None


class ResolveOutdatedDiscussionsUpdator(LocalUpdator):
    def update(self):
        if (
            "mergerequests" in self.rule
            and "resolve_outdated_diff_discussions" in self.rule.mergerequests
        ):
            mr_config = self.rule.mergerequests
            change_setting = ChangeSetting(
                property_name="resolve_outdated_diff_discussions",
                before=self.project.resolve_outdated_diff_discussions,
                after=mr_config.resolve_outdated_diff_discussions,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.resolve_outdated_diff_discussions = (
                mr_config.resolve_outdated_diff_discussions
            )
            return change_setting
        return None


class PrintMRLinkUpdator(LocalUpdator):
    def update(self):
        if (
            "mergerequests" in self.rule
            and "printing_merge_request_link_enabled" in self.rule.mergerequests
        ):
            mr_config = self.rule.mergerequests
            change_setting = ChangeSetting(
                property_name="printing_merge_request_link_enabled",
                before=self.project.printing_merge_request_link_enabled,
                after=mr_config.printing_merge_request_link_enabled,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.printing_merge_request_link_enabled = (
                mr_config.printing_merge_request_link_enabled
            )
            return change_setting
        return None


class RemoveSourceBranchUpdator(LocalUpdator):
    def update(self):
        if (
            "mergerequests" in self.rule
            and "remove_source_branch_after_merge" in self.rule.mergerequests
        ):
            mr_config = self.rule.mergerequests
            change_setting = ChangeSetting(
                property_name="remove_source_branch_after_merge",
                before=self.project.remove_source_branch_after_merge,
                after=mr_config.remove_source_branch_after_merge,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.remove_source_branch_after_merge = (
                mr_config.remove_source_branch_after_merge
            )
            return change_setting
        return None


class MergeMethodUpdator(LocalUpdator):
    def update(self):
        if "mergerequests" in self.rule and "merge_method" in self.rule.mergerequests:
            merge_method = self.rule.mergerequests.merge_method
            if merge_method not in MERGE_METHODS:
                raise ValueError(
                    f"Invalid merge method : '{merge_method}', expected : {MERGE_METHODS}"
                )
            change_setting = ChangeSetting(
                property_name="merge_method",
                before=self.project.merge_method,
                after=merge_method,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.merge_method = merge_method
            return change_setting
        return None


class SquashOptionUpdator(LocalUpdator):
    def update(self):
        if "mergerequests" in self.rule and "squash_option" in self.rule.mergerequests:
            squash_option = self.rule.mergerequests.squash_option
            if squash_option not in SQUASH_OPTIONS:
                raise ValueError(
                    f"Invalid squash option : '{squash_option}', expected : {SQUASH_OPTIONS.keys()}"
                )
            change_setting = ChangeSetting(
                property_name="squash_option",
                before=INV_SQUASH_OPTIONS[self.project.squash_option],
                after=squash_option,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.squash_option = SQUASH_OPTIONS[squash_option]
            return change_setting
        return None


class ResultPipelineUpdator(LocalUpdator):
    def update(self):
        if "mergerequests" in self.rule and "merge_pipelines_enabled" in self.rule.mergerequests:
            merge_pipelines_enabled = self.rule.mergerequests.merge_pipelines_enabled
            change_setting = ChangeSetting(
                property_name="merge_pipelines_enabled",
                before=self.project.merge_pipelines_enabled,
                after=merge_pipelines_enabled,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.merge_pipelines_enabled = merge_pipelines_enabled
            return change_setting

        return None


class MergeTrainUpdator(LocalUpdator):
    def update(self):
        if "mergerequests" in self.rule and "merge_trains_enabled" in self.rule.mergerequests:
            merge_trains_enabled = self.rule.mergerequests.merge_trains_enabled
            change_setting = ChangeSetting(
                property_name="merge_trains_enabled",
                before=self.project.merge_trains_enabled,
                after=merge_trains_enabled,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            self.project.merge_trains_enabled = merge_trains_enabled
            return change_setting
        return None


class TokenAccessUpdator(LocalUpdator):
    property_name = None  # type: str
    api_name = None  # type: str
    update_template = indent(
        """ mutation {{
                projectCiCdSettingsUpdate(
                    input: {{fullPath: "{path}", {ci_setting}: {value}}}
                    ) {{
                    ciCdSettings {{
                    {ci_setting}
                    }}
                    errors
                }}
            }}
        """,
        prefix="\n",
    )
    get_template = indent(
        """{{
            project(fullPath: "{path}") {{
                ciCdSettings {{
                   {ci_setting}
                }}
            }}
        }}""",
        prefix="\n",
    )

    def __init__(
        self,
        project: ProjectManager,
        rule: ProjectRule,
        show_diff_only: bool,
        sub_level: int = 0,
        params: Optional[GpcParameters] = None,
    ):
        super().__init__(project, rule, show_diff_only, sub_level)
        self.params = params

    def update(self):
        if "token_access" in self.rule and self.property_name in self.rule.token_access:
            change_setting = ChangeSetting(
                property_name=self.property_name,
                before=self.extract_current_setting(),
                after=self.rule.token_access[self.property_name],
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )

            if self.params.mode == RunMode.APPLY:
                new = "true" if self.rule.token_access[self.property_name] else "false"
                self.update_setting(new)

            return change_setting
        return None

    def extract_current_setting(self):
        gql = GraphqlSingleton()
        request_result = gql.run_graphql_query(
            query=self.get_template.format(
                path=self.project.attributes["path_with_namespace"], ci_setting=self.api_name
            )
        )
        return request_result["data"]["project"]["ciCdSettings"][self.api_name]

    def update_setting(self, new):
        gql = GraphqlSingleton()
        gql.run_graphql_query(
            query=self.update_template.format(
                path=self.project.attributes["path_with_namespace"],
                ci_setting=self.api_name,
                value=new,
            )
        )


class Allow_Token_Ci_Updator(TokenAccessUpdator):
    property_name = "allow_access_with_ci_job_token"
    api_name = "inboundJobTokenScopeEnabled"


class Limit_Token_Ci_Updator(TokenAccessUpdator):
    property_name = "limit_ci_job_token_access"
    api_name = "jobTokenScopeEnabled"


class CiJobTokenScope(LocalUpdator):
    property_name = None  # type: str
    add_api = "ciJobTokenScopeAddProject"
    remove_api = "ciJobTokenScopeRemoveProject"
    direction = None  # type: str
    get_template = indent(
        """{{
        project(fullPath: "{path}") {{
            ciJobTokenScope {{
                {prop} {{
                    edges {{
                        node {{
                        fullPath
        }} }} }} }} }} }}
        """,
        prefix="",
    )
    update_template = indent(
        """mutation
                             {{{operation}(input: {{projectPath:"{path}",
                             targetProjectPath:"{targetPath}", direction: {direction}}} )
                             {{ errors }} }}""",
        prefix="",
    )

    def __init__(
        self,
        project: ProjectManager,
        rule: ProjectRule,
        show_diff_only: bool,
        sub_level: int = 0,
        params: Optional[GpcParameters] = None,
    ):
        super().__init__(project, rule, show_diff_only, sub_level)
        self.params = params
        self.errors: List[dict] = []

    @cachedproperty
    def query_property(self):
        if self.direction == "INBOUND":
            return "inboundAllowlist"
        if self.direction == "OUTBOUND":
            return "outboundAllowlist"
        return None

    def update(self):
        if "token_access" in self.rule and self.property_name in self.rule.token_access:
            before = self.extract_current_setting()
            after = self.rule.token_access[self.property_name]
            change_setting = ChangeSetting(
                property_name=self.property_name,
                before=before,
                after=after,
                show_diff_only=self.show_diff_only,
                sub_level=self.sub_level,
            )
            if self.params.mode == RunMode.APPLY:
                to_remove = set(before) - set(after)
                to_add = set(after) - set(before)
                self.update_setting(to_remove, to_add)
            return change_setting
        return None

    def update_setting(self, to_remove, to_add):
        gql = GraphqlSingleton()
        for project in to_add:
            request_result = gql.run_graphql_query(
                query=self.update_template.format(
                    operation=self.add_api,
                    path=self.project.attributes["path_with_namespace"],
                    targetPath=project,
                    direction=self.direction,
                )
            )
            errors = request_result["data"][self.add_api]["errors"]
            if errors:
                self.errors.append({"project": project, "error": errors})
        for project in to_remove:
            request_result = gql.run_graphql_query(
                query=self.update_template.format(
                    operation=self.remove_api,
                    path=self.project.attributes["path_with_namespace"],
                    targetPath=project,
                    direction=self.direction,
                )
            )
            errors = request_result["data"][self.remove_api]["errors"]
            if errors:
                self.errors.append({"project": project, "error": errors})
        if self.errors:
            raise GpcError(f"Errors updating {self.property_name}:\n {self.errors}")

    def extract_current_setting(self):
        gql = GraphqlSingleton()
        request_result = gql.run_graphql_query(
            query=self.get_template.format(
                path=self.project.attributes["path_with_namespace"], prop=self.query_property
            )
        )
        res = [
            x["node"]["fullPath"]
            for x in request_result["data"]["project"]["ciJobTokenScope"][self.query_property][
                "edges"
            ]
        ]
        res.remove(self.project.attributes["path_with_namespace"])
        return res


class AllowList(CiJobTokenScope):
    property_name = "allowed_projects"
    direction = "INBOUND"


class LimitList(CiJobTokenScope):  # pylint: disable=too-many-lines
    property_name = "limited_projects"
    direction = "OUTBOUND"
