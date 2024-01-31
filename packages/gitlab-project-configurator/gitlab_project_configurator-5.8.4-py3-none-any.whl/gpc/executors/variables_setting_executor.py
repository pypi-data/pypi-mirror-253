"""
Make the update of environment variable.
"""

# Standard Library
import os
import re

from typing import Dict
from typing import Generator

# Third Party Libraries
import attr
import click

from boltons.cacheutils import cachedproperty
from dictns import Namespace
from gitlab.exceptions import GitlabListError
from structlog import get_logger

# Gitlab-Project-Configurator Modules
from gpc.change_setting import ChangePropertySetting
from gpc.executors.properties_updator import ChangePropertyExecutor
from gpc.helpers.exceptions import GpcPermissionError
from gpc.helpers.exceptions import GpcVariableError
from gpc.helpers.hider import hide_value
from gpc.parameters import RunMode
from gpc.property_manager import PropertyBean
from gpc.property_manager import PropertyManager


log = get_logger()

REGEX_MASKED_VARIABLE = r"^[a-zA-Z0-9+/\-\.\~_=:@]{8,}\Z"


@attr.s
class ProjectVariable(PropertyBean):
    protected = attr.ib()  # type: bool
    value = attr.ib()  # type: str
    is_hidden = attr.ib(default=False, hash=False, eq=False)  # type: bool
    warning_msg = attr.ib(default="")  # type: str
    variable_type = attr.ib(default="env_var")  # type: str
    masked = attr.ib(default=False)  # type: bool

    @staticmethod
    def to_project_variables(api_variables):
        project_variables = []
        for api_variable in api_variables:
            project_variables.append(ProjectVariable.to_project_variable(api_variable))
        return project_variables

    @staticmethod
    def to_project_variable(api_variable):
        protected = api_variable.protected if hasattr(api_variable, "protected") else False
        variable_type = (
            api_variable.variable_type if hasattr(api_variable, "variable_type") else "env_var"
        )
        masked = api_variable.masked if hasattr(api_variable, "masked") else False
        return ProjectVariable(
            name=api_variable.key,
            protected=protected,
            value=api_variable.value,
            variable_type=variable_type,
            masked=masked,
        )

    @cachedproperty
    def value_hidden(self):
        return hide_value(self.value)

    def get_query(self):
        return {
            "key": self.name,
            "protected": self.protected,
            "value": self.value,
            "variable_type": self.variable_type,
            "masked": self.masked,
        }

    def to_dict(self):
        dict_variable = {
            "name": self.name,
            "protected": self.protected,
            "warning": self.warning_msg,
            "variable_type": self.variable_type,
            "masked": self.masked,
        }
        if self.is_hidden:
            dict_variable["value"] = self.value_hidden
        else:
            dict_variable["value"] = self.value
        return dict_variable


class ChangeVariables(ChangePropertySetting):
    sub_properties = ["protected", "value", "variable_type", "masked"]
    status_to_process = ["removed", "updated", "kept", "added", "warning"]

    def _generate_diff(self, before_name, before, after_properties):
        current_diff = self._is_warning(before_name, before, after_properties)
        if not current_diff:
            current_diff = super()._generate_diff(before_name, before, after_properties)
        return current_diff

    def _removed(self, before_name, before, after_properties):
        result = {}
        if before_name in after_properties and after_properties[before_name].value is None:
            before.is_hidden = before.protected
            result = {
                "status": "removed",
                "before": before.to_dict(),
                "after": after_properties[before_name].to_dict(),
            }
        if not result:
            before.is_hidden = before.protected
            result = super()._removed(before_name, before, after_properties)
        return result

    def _is_kept(self, before_name, before, after_properties):
        if before_name in after_properties and after_properties[before_name].value is None:
            return {}
        if self.keep_existing:
            before.is_hidden = before.protected
        elif before_name in after_properties and before == after_properties[before_name]:
            before.is_hidden = after_properties[before_name].is_hidden
        return super()._is_kept(before_name, before, after_properties)

    def _is_updated(self, before_name, before, after_properties):
        result = super()._is_updated(before_name, before, after_properties)
        if result and after_properties[before_name].value is not None:
            before.is_hidden = after_properties[before_name].is_hidden
            result["before"] = before.to_dict()
        else:
            result = {}
        return result

    def _is_warning(self, before_name, before, after_properties):
        result = {}
        if before_name in after_properties:
            if after_properties[before_name].warning_msg:
                after_prop = after_properties[before_name].to_dict()
                before.is_hidden = True
                result = {
                    "status": "warning",
                    "before": before.to_dict(),
                    "after": after_prop,
                }
        return result

    def _added_properties(self, differences: Dict, after_properties: Dict, **kwargs):
        for name, prop in after_properties.items():
            status = "warning" if prop.warning_msg else "added"
            if name not in differences:
                differences[name] = {
                    "status": status,
                    "before": None,
                    "after": prop.to_dict(),
                }

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
        table_rows.append("new_line")

        for change in self.differences.values():
            line_color = self.get_line_color(change["status"])

            name_before = change["before"]["name"] if change["before"] else ""
            name_after = change["after"]["name"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("name", console, "property_name"),
                        self.wrap_text(name_before, console, "before"),
                        self.wrap_text(name_after, console, "after"),
                        change["status"],
                    ),
                    line_color,
                )
            )
            protected_before = change["before"]["protected"] if change["before"] else ""
            protected_after = change["after"]["protected"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("protected", console, "property_name"),
                        self.wrap_text(str(protected_before), console, "before"),
                        self.wrap_text(str(protected_after), console, "after"),
                        "",
                    ),
                    line_color,
                )
            )

            warning_before = change["before"]["warning"] if change["before"] else ""
            warning_after = change["after"]["warning"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("warning", console, "property_name"),
                        self.wrap_text(warning_before, console, "before"),
                        self.wrap_text(warning_after, console, "after"),
                        "",
                    ),
                    line_color,
                )
            )

            variable_type_before = change["before"]["variable_type"] if change["before"] else ""
            variable_type_after = change["after"]["variable_type"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("variable_type", console, "property_name"),
                        self.wrap_text(variable_type_before, console, "before"),
                        self.wrap_text(variable_type_after, console, "after"),
                        "",
                    ),
                    line_color,
                )
            )
            masked_before = change["before"]["masked"] if change["before"] else ""
            masked_after = change["after"]["masked"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("masked", console, "property_name"),
                        self.wrap_text(str(masked_before), console, "before"),
                        self.wrap_text(str(masked_after), console, "after"),
                        "",
                    ),
                    line_color,
                )
            )

            value_before = change["before"]["value"] if change["before"] else ""
            value_before = (
                "[MASKED]" if change["before"] and change["before"]["masked"] else value_before
            )
            value_after = change["after"]["value"] if change["after"] else ""
            table_rows.append(
                (
                    (
                        self.wrap_text("value", console, "property_name"),
                        self.wrap_text(value_before, console, "before"),
                        self.wrap_text(value_after, console, "after"),
                        "",
                    ),
                    line_color,
                )
            )
            table_rows.append("new_line")

        table_rows.append("new_section")
        return table_rows


class VariablesSettingExecutor(ChangePropertyExecutor):
    order = 40
    name = "variables"
    applicable_to = ["group", "project"]
    sections = ["variables"]

    @property
    def variables(self):
        if "variables" not in self.rule or self.rule.variables is None:
            return None
        return self.rule.variables

    def _apply(self):
        if self.changes:
            variables = self.changes[0]
            self._save_properties(
                PropertyManager(self.project.variables), variables, variables.after
            )

    def _update(self, mode: RunMode, members_user, members_group):
        if "variables" not in self.rule or self.rule.variables is None:
            return

        keep_existing_variables = self.rule.get("keep_existing_variables", False)
        previous_variables = ProjectVariable.to_project_variables(
            self.project.variables.list(as_list=False, retry_transient_errors=True)  # type: ignore
        )

        preparator = VariablesSettingPreparator(
            self.project_path, self.rule, self.rule.variables, self.warnings
        )
        env_variables = preparator.prepare_variables(mode)

        try:
            self.changes.append(
                ChangeVariables(
                    property_name="variables",
                    before=sorted(previous_variables, key=lambda x: x.name),
                    after=sorted(env_variables, key=lambda x: x.name),
                    show_diff_only=self.show_diff_only,
                    keep_existing=keep_existing_variables,
                )
            )
        except GitlabListError as e:
            # Check if pipeline is enabled
            if e.response_code == 403 and not self.project.jobs_enabled:  # type: ignore
                error_message = (
                    f"ERROR on project {self.project_path}: Environment variables can not be set. "
                    "Please ensure Pipelines are enabled "
                    "on your project"
                )
                raise GpcPermissionError(error_message) from e
            raise


class VariablesSettingPreparator:
    def __init__(self, project_path, rule, variables, warnings):
        self.rule = rule
        self.variables = variables
        self.project_path = project_path
        self.warnings = warnings

    def prepare_variables(self, mode):
        env_variables = []

        for env_variable in self._expand_variables():
            name = env_variable.name
            variable_type = (
                env_variable.variable_type if hasattr(env_variable, "variable_type") else "env_var"
            )
            protected = self.is_protected_variable(env_variable)
            value = env_variable.get("value", None)
            masked = env_variable.get("masked", False)
            value_from_envvar = env_variable.get("value_from_envvar", None)
            is_hidden = False
            is_hidden, value, warning_msg = self._extract_value(
                is_hidden, mode, value, value_from_envvar, masked, protected
            )
            if masked and value:
                VariablesSettingPreparator.validate_value(name, value)

            env_variables.append(
                ProjectVariable(
                    name=name,
                    protected=protected,
                    value=value,
                    is_hidden=is_hidden,
                    variable_type=variable_type,
                    masked=masked,
                    warning_msg=warning_msg,
                )
            )
        return env_variables

    def is_protected_variable(self, env_variable):
        return env_variable.get("protected", False)

    def _extract_value(self, is_hidden, mode, value, value_from_envvar, masked, protected):
        warning_msg = ""
        if value_from_envvar:
            if os.getenv(value_from_envvar) is not None:
                value = os.getenv(value_from_envvar)
                if masked or protected:
                    is_hidden = True
            else:
                warning_msg = f"/!\\ Environment variable {value_from_envvar} not found."
                if mode is RunMode.DRY_RUN:
                    self.warnings.append(warning_msg)
                    click.secho(warning_msg, fg="red")
                    click.secho(
                        "/!\\ In Apply or Interactive mode your configuration will fail.",
                        fg="yellow",
                    )
                else:
                    raise ValueError(warning_msg)
        if isinstance(value, bool):
            value = str(value).lower()
        else:
            value = str(value) if value is not None else None
        return is_hidden, value, warning_msg

    def _expand_variables(self) -> Generator[Namespace, None, None]:
        """I inject the variable_profiles when applicable."""
        for variable in self.variables:
            if "import" in variable:
                var_profile_name = variable.get("import")
                log.debug(f"Injecting variable profile from : {var_profile_name}")
                if not self.rule.get("variable_profiles") or not self.rule.get(
                    "variable_profiles", {}
                ).get(var_profile_name):
                    raise GpcVariableError(
                        f"On project {self.project_path}: "
                        f"The import of variable {var_profile_name} is impossible, because "
                        "this variable is not found "
                        "in the 'variable_profiles' section."
                    )
                yield from self.rule.get("variable_profiles", {}).get(var_profile_name, [])
            else:
                yield variable

    @staticmethod
    def validate_value(name, value):
        if not re.match(REGEX_MASKED_VARIABLE, value):
            raise GpcVariableError(
                f"The '{name}' value does not respect the requirements"
                " for masked variable. See the requirements here: "
                "https://docs.gitlab.com/ee/ci/variables/index.html#mask-a-cicd-variable"
            )
