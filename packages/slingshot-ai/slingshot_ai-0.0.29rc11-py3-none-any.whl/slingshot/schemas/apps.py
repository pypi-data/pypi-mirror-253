from typing import Annotated, Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, model_validator
from typing_extensions import override

from slingshot.sdk import backend_schemas
from slingshot.sdk.graphql import fragments
from slingshot.shared.validation_warnings import SlingshotDeprecationWarning, record_validation_warning

from .components import AbstractComponentSpec
from .environments import EnvironmentSpec
from .mixins import (
    ComponentConfigMixin,
    ComponentEnvironmentMixin,
    ComponentMountsMixin,
    ComponentProjectCredentialsMixin,
    ScriptBasedComponentMixin,
)
from .mounts import DownloadMountSpec, MountSelector, MountSpecUnion, MountTarget, UploadMountSpec
from .runs import RunSpec


class AbstractAppSpec(AbstractComponentSpec):
    """
    Base class for all "app" types, including (custom) webapps and supported third party apps.
    """

    model_config = ConfigDict(title="App")

    using: Literal['webapp', 'session', 'redis', 'label-studio'] = Field(
        ..., title="Using", description="Which package to use. Set to webapp for a custom web application."
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.component_type != backend_schemas.ComponentType.APP:
            raise ValueError(f"Cannot diff an app against a non-app.")

        return super().diff(existing)

    @override
    @classmethod
    def silent_default_machine_type(cls) -> backend_schemas.MachineType | None:
        # We're defaulting silently for apps, see https://linear.app/slingshotai/issue/ENG-1998
        return backend_schemas.MachineType.CPU_SMALL


class WebappComponentSpec(AbstractAppSpec, ScriptBasedComponentMixin):
    using: Literal['webapp'] = Field(
        ..., title="Using", description="Which package to use. Set to webapp for a custom web application."
    )
    port: Optional[int] = Field(None, title="Port", description="The port to expose.")

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.app_sub_type != backend_schemas.AppSubType.WEBAPP:
            raise ValueError(f"Cannot change the type of an existing app, create a new app instead.")

        diff = super().diff(existing)
        if self.port != existing.app_port:
            diff.append(f"Port changed from '{existing.app_port}' → '{self.port}'")
        return diff


# TODO: Allow users to not specify envs for Sessions
class SessionComponentSpec(
    ComponentEnvironmentMixin,
    ComponentMountsMixin,
    ComponentProjectCredentialsMixin,
    ComponentConfigMixin,
    AbstractAppSpec,
):
    model_config = ConfigDict(title="Session")
    using: Literal['session'] = Field(
        ...,
        title="Using",
        description="Which package to use. When specified, this feature automatically adjusts the behavior of the app.",
    )

    @property
    def port(self) -> int:
        return 8080

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.app_sub_type != backend_schemas.AppSubType.SESSION:
            raise ValueError(f"Cannot change the type of an existing app, create a new app instead.")

        diff = super().diff(existing)
        if self.port != existing.app_port:
            diff.append(f"Port changed from '{existing.app_port}' → '{self.port}'")
        return diff


class RedisComponentSpec(AbstractAppSpec):
    using: Literal['redis'] = Field(
        ...,
        title="Using",
        description="Which package to use. When specified, this feature automatically adjusts the behavior of the app.",
    )

    @property
    def port(self) -> int:
        return 6379

    def get_mounts(self) -> list[MountSpecUnion]:
        return []

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.app_sub_type != backend_schemas.AppSubType.REDIS:
            raise ValueError(f"Cannot change the type of an existing app, create a new app instead.")

        diff = super().diff(existing)
        if self.port != existing.app_port:
            diff.append(f"Port changed from '{existing.app_port}' → '{self.port}'")
        return diff


class LabelStudioComponentSpec(AbstractAppSpec):
    using: Literal['label-studio'] = Field(
        ...,
        title="Using",
        description="Which package to use. When specified, this feature automatically adjusts the behavior of the app.",
    )

    import_run: str = Field(
        "sync-to-label-studio",
        title="Sync to Label Studio",
        description="The name of the run used to sync data to Label Studio.",
    )

    export_run: str = Field(
        "sync-from-label-studio",
        title="Sync annotations from Label Studio",
        description="The name of the run used to sync data from Label Studio.",
    )

    def get_mounts(self) -> list[MountSpecUnion]:
        return []

    @staticmethod
    def get_default_import_run() -> RunSpec:
        return RunSpec(
            name="sync-to-label-studio",
            environment="label-studio-run-env",
            machine_type=backend_schemas.MachineType.CPU_SMALL,
            cmd="python label_studio/sync_to_label_studio.py",
            mounts=[
                DownloadMountSpec(mode="DOWNLOAD", path="/mnt/data", selector=MountSelector(name="dataset")),
                DownloadMountSpec(mode="DOWNLOAD", path="/mnt/annotations", selector=MountSelector(name="annotations")),
            ],
        )

    @staticmethod
    def get_default_export_run() -> RunSpec:
        return RunSpec(
            name="sync-from-label-studio",
            environment="label-studio-run-env",
            machine_type=backend_schemas.MachineType.CPU_SMALL,
            cmd="python label_studio/sync_from_label_studio.py",
            mounts=[UploadMountSpec(mode="UPLOAD", path="/mnt/annotations", target=MountTarget(name="annotations"))],
            attach_project_credentials=True,
        )

    @staticmethod
    def get_default_run_environment() -> EnvironmentSpec:
        return EnvironmentSpec(python_packages=["label-studio-sdk>=0.0.30", "slingshot-ai"])

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        """Returns a list of differences between this and another app spec."""
        if existing.app_sub_type != backend_schemas.AppSubType.LABEL_STUDIO:
            raise ValueError(f"Cannot diff Label Studio app against other component type.")
        diff = super().diff(existing)
        # TODO: Add diff for import/export runs
        return diff


AppSpecUnion = Annotated[
    Union[SessionComponentSpec, RedisComponentSpec, LabelStudioComponentSpec, WebappComponentSpec],
    Field(discriminator='using'),
]


class SafeAppSpec(RootModel[AppSpecUnion]):
    """
    Reads an app spec with extra validation for missing 'using'. Using a root model appears to be the only way to add
    validation before Pydantic picks the specific class to validate - this significantly improves the error message
    when no 'using' is specified.
    """

    @model_validator(mode='before')
    @classmethod
    def require_sub_type_to_be_specified(cls, data: Any) -> Any:
        if isinstance(data, BaseModel):
            data = data.model_dump()

        if 'using' not in data or not data['using']:
            record_validation_warning(
                SlingshotDeprecationWarning("Specifying 'using' for an app is required since version 0.0.19")
            )

            raise ValueError("Apps require a 'using' field to be specified, use 'webapp' for a custom web application")
        return data
