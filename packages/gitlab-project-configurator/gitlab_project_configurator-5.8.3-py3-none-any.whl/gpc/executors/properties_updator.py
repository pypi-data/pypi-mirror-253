"""
Change executor abstract class.
"""

# Third Party Libraries
import click

from gitlab import Gitlab
from gitlab.exceptions import GitlabCreateError
from gitlab.exceptions import GitlabDeleteError
from gitlab.exceptions import GitlabGetError
from gitlab.v4.objects import ProjectManager

# Gitlab-Project-Configurator Modules
from gpc.executors.change_executor import ChangeExecutor
from gpc.helpers.types import ProjectRule
from gpc.parameters import GpcParameters


# pylint: disable= abstract-method


class PropertyUpdatorMixin:
    def _save_properties(self, manager, change_properties, properties):
        for name in change_properties.remove:
            try:
                manager.rm_existing(name)
            except GitlabDeleteError as e:
                click.secho(f"ERROR: {str(e.error_message)}", fg="red")
        self._update_or_create(manager, change_properties, properties)

    def _update_or_create(self, manager, change_properties, properties):
        # target to update or create
        variables_to_cu = change_properties.update_or_create
        for variable in properties:
            if variable.name in variables_to_cu:
                try:
                    manager.create(variable, self.project_path)
                except GitlabCreateError as e:
                    click.secho(f"ERROR: {str(e.error_message)}", fg="red")


class ChangePropertyExecutor(ChangeExecutor, PropertyUpdatorMixin):
    pass


class ChangeServicePropertyExecutor(ChangePropertyExecutor):
    service_name = ""

    def __init__(
        self,
        gl: Gitlab,
        project_path: str,
        project: ProjectManager,
        rule: ProjectRule,
        gpc_params: GpcParameters,
    ):
        super().__init__(gl, project_path, project, rule, gpc_params)
        self._service = None

    @property
    def service(self):
        if self._service is None:
            try:
                self._service = self.project.services.get(
                    self.service_name, retry_transient_errors=True
                )
            except GitlabGetError:
                # In case service is not found new gitlab api return a 404
                # To resolve that, calling delete api will create an deactivated service
                self.project.services.delete(id=self.service_name, retry_transient_errors=True)
                self._service = self.project.services.get(
                    self.service_name, retry_transient_errors=True
                )

        return self._service

    def _apply(self):
        if self.service_name.lower() in self.gpc_params.force:
            click.secho(f"'{self.service_name}': settings force updated!", fg="yellow")
            self.service.save(retry_transient_errors=True)
        elif self.changes:
            service_property = self.changes[0]
            if not service_property.has_diff():
                return
            if service_property.after.disabled:
                self.service.delete(retry_transient_errors=True)
            else:
                self.service.save(retry_transient_errors=True)
