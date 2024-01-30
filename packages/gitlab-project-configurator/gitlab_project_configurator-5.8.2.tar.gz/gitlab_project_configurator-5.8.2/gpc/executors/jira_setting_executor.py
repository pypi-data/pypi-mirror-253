"""
Up the jira services.
"""

# Standard Library
import os

from typing import Optional  # pylint: disable=unused-import
from typing import Union  # pylint: disable=unused-import

# Third Party Libraries
import attr
import click

from boltons.cacheutils import cachedproperty

# Gitlab-Project-Configurator Modules
from gpc.change_setting import ChangeSettingSubProperty
from gpc.executors.properties_updator import ChangeServicePropertyExecutor
from gpc.helpers.hider import hide_value
from gpc.parameters import RunMode
from gpc.property_manager import PropertyBean


@attr.s(eq=False)
class JiraProperty(PropertyBean):
    url = attr.ib(default=None)  # type: str
    jira_issue_transition_id = attr.ib(default=None)  # type: int
    disabled = attr.ib(default=False)  # type: bool
    username = attr.ib(default=None)  # type: str
    password = attr.ib(default=None)  # type: str
    trigger_on_commit = attr.ib(default=False)  # type: Optional[bool]
    trigger_on_mr = attr.ib(default=True)  # type: Optional[bool]
    comment_on_event_enabled = attr.ib(default=False)  # type: Optional[Union[bool, str]]
    warning_msg = attr.ib(default=None)  # type: str

    @staticmethod
    def to_jira_property(api_jira_setting):
        jira_property = JiraProperty(name="jira")
        jira_property.url = api_jira_setting.properties.get("url", None)
        jira_property.username = api_jira_setting.properties.get("username", None)
        jira_property.password = api_jira_setting.properties.get("password", None)
        jira_property.jira_issue_transition_id = api_jira_setting.properties.get(
            "jira_issue_transition_id", None
        )
        jira_property.trigger_on_commit = api_jira_setting.commit_events
        jira_property.trigger_on_mr = api_jira_setting.merge_requests_events
        jira_property.comment_on_event_enabled = api_jira_setting.comment_on_event_enabled
        if hasattr(api_jira_setting, "active"):
            jira_property.disabled = not api_jira_setting.active
        return jira_property

    def get_query(self):
        pass

    def to_dict(self):
        to_dict = {
            "name": self.name,
            "url": self.url,
            "username": self.username,
            "jira_issue_transition_id": self.jira_issue_transition_id,
            "trigger_on_commit": self.trigger_on_commit,
            "trigger_on_mr": self.trigger_on_mr,
            "comment_on_event_enabled": self.comment_on_event_enabled,
        }
        if self.warning_msg:
            to_dict["warning"] = self.warning_msg
        to_dict["password"] = hide_value(self.password)
        return to_dict

    def __eq__(self, other):
        if not isinstance(other, JiraProperty):
            return False
        eq = (
            self.name == other.name
            and self.url == other.url
            and self.username == other.username
            and self.jira_issue_transition_id == other.jira_issue_transition_id
            and self.disabled == other.disabled
            and self.trigger_on_commit == other.trigger_on_commit
            and self.trigger_on_mr == other.trigger_on_mr
            and self.comment_on_event_enabled == other.comment_on_event_enabled
        )
        return eq


@attr.s
class ChangeJiraProperty(ChangeSettingSubProperty):
    def to_dict(self):
        return {
            "property_name": self.property_name,
            "differences": {
                "jira": {
                    "before": self.before.to_dict(),
                    "after": self.after.to_dict(),
                    "action": self.action,
                }
            },
        }

    @cachedproperty
    def action(self):
        if self.after.disabled:
            return "removed"
        if self.after.warning_msg:
            return "warning"
        if self.after == self.before:
            return "kept"
        return "updated"


class JiraSettingExecutor(ChangeServicePropertyExecutor):
    order = 70
    name = "jira"
    sections = ["integrations"]
    service_name = "jira"

    def _update(self, mode: RunMode, members_user, members_group):
        if "integrations" not in self.rule or "jira" not in self.rule.integrations:
            return
        setting = self.rule.integrations.jira
        jira_property = JiraProperty(name="jira")
        disabled = setting.get("disabled", False)
        before_settings = JiraProperty.to_jira_property(self.service)
        jira_property.disabled = disabled
        if not disabled:
            jira_property.url = setting.get("url")
            transition_ids = setting.get("jira_issue_transition_id", None)
            if transition_ids == "":
                # If the config value is an empty string, we want to remove the
                # jira_issue_transition_id on server.
                transition_ids = None
            elif transition_ids is not None:
                transition_ids = str(transition_ids)
            else:
                # If None we want to keep the existing value.
                transition_ids = before_settings.jira_issue_transition_id
            jira_property.jira_issue_transition_id = transition_ids
            jira_property.username = (
                os.getenv(setting.get("username_from_envvar"))
                if "username_from_envvar" in setting
                else setting.get("username")
            )
            jira_property.trigger_on_commit = setting.get("trigger_on_commit", False)
            jira_property.comment_on_event_enabled = setting.get("comment_on_event_enabled", False)
            jira_property.trigger_on_mr = setting.get("trigger_on_mr", True)
            self._set_password(jira_property, setting, mode)
        self.changes.append(
            ChangeJiraProperty(
                property_name="jira",
                before=before_settings,
                after=jira_property,
                show_diff_only=self.show_diff_only,
            )
        )
        self.service.url = jira_property.url
        self.service.username = jira_property.username
        self.service.password = jira_property.password
        self.service.jira_issue_transition_id = jira_property.jira_issue_transition_id
        self.service.commit_events = jira_property.trigger_on_commit
        self.service.comment_on_event_enabled = jira_property.comment_on_event_enabled
        self.service.merge_requests_events = jira_property.trigger_on_mr

    def _set_password(self, jira_property: JiraProperty, setting, mode: RunMode):
        if (
            setting.get("password_from_envvar")
            and os.getenv(setting.get("password_from_envvar")) is not None
        ):
            jira_property.password = os.getenv(setting.get("password_from_envvar"), "")
        else:
            warning_msg = (
                f"/!\\ Environment variable {setting.get('password_from_envvar')} " "not found."
            )
            click.secho(warning_msg, fg="red")
            if mode is RunMode.DRY_RUN:
                self.warnings.append(warning_msg)
                click.secho(
                    "/!\\ In Apply or Interactive mode your configuration will fail.",
                    fg="yellow",
                )
                jira_property.password = ""  # nosec
                jira_property.warning_msg = warning_msg
            else:
                raise ValueError(warning_msg)
