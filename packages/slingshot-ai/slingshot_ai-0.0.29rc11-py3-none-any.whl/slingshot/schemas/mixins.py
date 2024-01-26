import json
from typing import Any

import deepdiff
from pydantic import Field, field_validator
from typing_extensions import override

from slingshot.sdk.graphql import fragments

from .components import AbstractComponentSpec
from .mounts import MountSpecUnion, diff_mount_spec


class ComponentMountsMixin(AbstractComponentSpec):
    """Mixin for including mount support including validation."""

    mounts: list[MountSpecUnion] = Field(default_factory=list, title="Mounts", description="The mounts to be attached.")

    @override
    def get_mounts(self) -> list[MountSpecUnion]:
        return self.mounts

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        diff = super().diff(existing)

        my_mount_path = {f"{i.mode}: {i.path}": i for i in self.mounts}
        existing_mounts = {f"{i.mode}: {i.path}": i for i in existing.mount_specs}
        added_keys = set(my_mount_path.keys()) - set(existing_mounts.keys())
        for i in added_keys:
            diff.append(f"Added mount '{i}'")
        removed_keys = set(existing_mounts.keys()) - set(my_mount_path.keys())
        for i in removed_keys:
            diff.append(f"Removed mount '{i}'")
        same_path = set(existing_mounts.keys()) & set(my_mount_path.keys())
        for i in same_path:
            existing_mount = existing_mounts[i]
            new = my_mount_path[i]
            d = diff_mount_spec(new, existing_mount)
            if d:
                diff.append(f"Changed mount '{i}': {d}")

        return diff

    @field_validator("mounts")
    @classmethod
    def validate_mount_paths_unique(cls, v: list[MountSpecUnion]) -> list[MountSpecUnion]:
        """
        Verify that all mount paths are unique. We add an explicit message for the case of a download path conflicting
        with an upload path as prior to Aug 2023 this used to be supported.
        """
        download_paths = [str(spec.path) for spec in v if spec.mode == "DOWNLOAD"]
        upload_paths = [str(spec.path) for spec in v if spec.mode == "UPLOAD"]
        all_mount_paths = [str(spec.path) for spec in v]

        # TODO: mention which paths are conflicting in the error
        if set(download_paths).intersection(set(upload_paths)):
            raise ValueError("The same mount path cannot be used for both upload and download.")
        if len(all_mount_paths) != len(set(all_mount_paths)):
            raise ValueError("Mount paths must be unique across all mounts")

        return v


class ComponentConfigMixin(AbstractComponentSpec):
    config_variables: dict[str, Any] = Field(
        default_factory=dict, title="Arguments", description="Optional user defined arguments to pass to the app."
    )

    @field_validator("config_variables", mode='before')
    @classmethod
    def show_nicer_error_for_nested_config_variables(cls, v: dict[str, Any]) -> dict[str, Any]:
        """
        Pydantic will enforce this already but the errors aren't pretty, do a manual check here.
        """
        if not isinstance(v, dict):
            raise ValueError("config_variables must be a mapping")

        return v

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        """Returns a list of differences between this and another component spec."""
        diff = super().diff(existing)
        config_variables = json.loads(existing.config_variables) if existing.config_variables else {}

        if deepdiff.DeepDiff(config_variables, self.config_variables, ignore_order=True):
            diff.append(f'Config variables changed from {config_variables} → {self.config_variables}')
        return diff


class ComponentEnvironmentMixin(AbstractComponentSpec):
    environment: str = Field(..., title="Environment", description="The name of the environment.")

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        diff = super().diff(existing)
        env_spec = existing.execution_environment_spec
        environment = env_spec.execution_environment_spec_name if env_spec else None
        if self.environment != environment:
            diff.append(f"Environment changed from '{environment}' → '{self.environment}'")
        return diff


class ComponentProjectCredentialsMixin(AbstractComponentSpec):
    attach_project_credentials: bool = Field(
        True,
        title="Attach project credentials",
        description=(
            "If true, will make an API key available to instances under the `SLINGSHOT_API_KEY` environment"
            "variable so that they can make requests using the Slingshot SDK for this project"
        ),
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        diff = super().diff(existing)

        if self.attach_project_credentials and not existing.service_account:
            diff.append(f"Project credentials added")
        elif not self.attach_project_credentials and existing.service_account:
            diff.append(f"Project credentials removed")
        return diff


class ScriptBasedComponentMixin(
    ComponentEnvironmentMixin,
    ComponentMountsMixin,
    ComponentConfigMixin,
    ComponentProjectCredentialsMixin,
    AbstractComponentSpec,
):
    """
    Mixin for all "script based" component specs.

    These all share common properties such as an environment, a command to run, a list of mounts, etc.
    """

    cmd: str = Field(..., title="Command", description="The command to run.")

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        diff = super().diff(existing)

        if self.cmd != existing.command:
            diff.append(f"Command changed from '{existing.command}' → '{self.cmd}'")

        return diff
