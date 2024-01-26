import typing
from typing import Any, Literal

from pydantic import ConfigDict, Field, field_validator, model_validator
from typing_extensions import Self, override

from slingshot.sdk.errors import SlingshotException
from slingshot.shared.validation_warnings import SlingshotDeprecationWarning, record_validation_warning

from .apps import AppSpecUnion, LabelStudioComponentSpec, SafeAppSpec, SessionComponentSpec
from .common import FILE_LOCATION, SlingshotBaseModel
from .components import AbstractComponentSpec
from .deployments import AbstractDeploymentSpec, DeploymentSpecUnion, SafeDeploymentSpec
from .environments import EnvironmentSpec
from .runs import RunSpec
from .sources import SourceMapping

if typing.TYPE_CHECKING:
    from pydantic.main import IncEx

LOCAL_ONLY_MANIFEST_SECTIONS = ['sources']


class ProjectManifest(SlingshotBaseModel):
    model_config = ConfigDict(
        title="Slingshot Config Spec",
        from_attributes=True,
        json_schema_extra={"$schema": "http://json-schema.org/draft/2020-12/schema", "$id": FILE_LOCATION},
    )

    environments: dict[str, EnvironmentSpec] = Field(
        default_factory=dict, title="Environments", description="The environments to use for the job."
    )
    apps: list[AppSpecUnion] = Field(default_factory=list, title=AbstractComponentSpec.model_config["title"])
    runs: list[RunSpec] = Field(default_factory=list, title=RunSpec.model_config["title"])
    deployments: list[DeploymentSpecUnion] = Field(
        default_factory=list, title=AbstractDeploymentSpec.model_config["title"]
    )
    sources: list[SourceMapping] | None = Field(
        None,
        title="Sources",
        description="Sources to include for Slingshot components. If not set, the project directory will be used. "
        "Can be set to an empty list to explicitly disable sources.",
    )

    @override
    def model_dump(
        self,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        by_alias: bool = False,
        include: "IncEx" = None,
        exclude: "IncEx" = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = True,  # Overriden from Pydantic defaults
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True,
        # If true, sections of the manifest that are local only (not not pushed to Slingshot) will be excluded,
        # if false (the default), all sections will be included.
        exclude_local_only: bool = False,
    ) -> dict[str, Any]:
        # We override the include/exclude logic, users shoudn't pass explicit values
        assert include is None and exclude is None, "The project manifest doesn't support include/exclude"

        if exclude_local_only:
            exclude = set(LOCAL_ONLY_MANIFEST_SECTIONS)

        res = super().model_dump(
            mode=mode,
            exclude=exclude,
            by_alias=by_alias,
            exclude_none=exclude_none,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            round_trip=round_trip,
            warnings=warnings,
        )

        # We usually want "exclude_defaults" so as to not fill up our slingshot.yaml with a lot of redundant values
        # when pulling in remote changes, but the top level definitions are different. We always populate them as a
        # placeholder to the user and to make diffs cleaner when environments and components are added for the first
        # time. To get the behaviour that we want without passing "exclude_defaults" to the child models, we explicitly
        # populate the empty objects here.
        if 'environments' not in res:
            res['environments'] = dict()
        if 'apps' not in res:
            res['apps'] = []
        if 'runs' not in res:
            res['runs'] = []
        if 'deployments' not in res:
            res['deployments'] = []

        return res

    @field_validator('apps', mode='before')
    @classmethod
    def complain_if_missing_using_in_app(cls, value: Any) -> list[Any]:
        if isinstance(value, list):
            return [SafeAppSpec.model_validate(app).root for app in value]
        else:
            return value

    @field_validator('deployments', mode='before')
    @classmethod
    def default_deployment_spec_to_custom(cls, value: Any) -> list[Any]:
        if isinstance(value, list):
            return [SafeDeploymentSpec.model_validate(app).root for app in value]
        else:
            return value

    @model_validator(mode="after")
    def slingshot_yaml_global_validator(self) -> Self:
        _validate_label_studio_runs(self)
        # Must be before env validation, since it might add new envs
        _validate_environments_are_defined(self)
        _validate_session_environments(self)
        _validate_source_mappings_are_unique(self)
        return self

    @model_validator(mode='before')
    @classmethod
    def check_machine_deprecations(cls, manifest: dict[str, Any]) -> dict[str, Any]:
        all_apps_runs_deployments = []
        all_apps_runs_deployments.extend(manifest['apps'] if 'apps' in manifest else [])
        all_apps_runs_deployments.extend(manifest['runs'] if 'runs' in manifest else [])
        all_apps_runs_deployments.extend(manifest['deployments'] if 'deployments' in manifest else [])

        # Check old GPUs
        for app_run_deployment in all_apps_runs_deployments:
            machine_type = app_run_deployment['machine_type'] if 'machine_type' in app_run_deployment else None
            if machine_type in {"GPU", "GPU_A100"}:
                record_validation_warning(
                    SlingshotDeprecationWarning(
                        f"Machine type '{machine_type}' is not supported in slingshot.yaml (since version '0.0.10'). "
                        + "Hint: Use 'slingshot machines' for machine options."
                    )
                )

        return manifest


def _validate_environments_are_defined(manifest: ProjectManifest) -> None:
    """Validate that all referenced environments are in the environments list"""
    envs: dict[str, EnvironmentSpec] = manifest.environments
    for app_or_run_or_deployment in [*manifest.apps, *manifest.runs, *manifest.deployments]:
        env = getattr(app_or_run_or_deployment, "environment", None)
        if env and env not in envs:
            name = getattr(app_or_run_or_deployment, "name", None)
            raise SlingshotException(
                f"Environment '{env}' used in '{name}' not found in 'environments' {list(envs.keys())}"
            )


def _validate_session_environments(manifest: ProjectManifest) -> None:
    sessions = [app for app in manifest.apps if isinstance(app, SessionComponentSpec)]
    envs: dict[str, EnvironmentSpec] = manifest.environments
    session_envs = {session.environment: envs[session.environment] for session in sessions if session.environment}

    for session_env_name, session_env in session_envs.items():
        requested_python_requirements = session_env.python_packages
        if not any("jupyterlab" in requirement for requirement in requested_python_requirements):
            raise SlingshotException(
                f"'jupyterlab' was not found in the '{session_env_name}' environment. Please add it and try again."
            )


def _validate_label_studio_runs(manifest: ProjectManifest) -> None:
    """Make sure Label Studio is set up correctly"""
    label_studio_apps = [app for app in manifest.apps if isinstance(app, LabelStudioComponentSpec)]
    if not label_studio_apps:
        return
    if len(label_studio_apps) > 1:
        app_names = [app.name for app in label_studio_apps]
        # TODO: Implement logic for multiple label studio apps
        raise SlingshotException(f"Only one label studio app is supported per Slingshot Project. Found {app_names}")

    runs: list[RunSpec] = manifest.runs
    import_run_name = label_studio_apps[0].import_run
    export_run_name = label_studio_apps[0].export_run
    label_studio_app_name = label_studio_apps[0].name

    if import_run_name not in [run.name for run in runs]:
        raise SlingshotException(
            f"Run '{import_run_name}' (used as the 'import_run' for {label_studio_app_name}) was not found in "
            "'runs'. Please add it and try again."
        )

    if export_run_name not in [run.name for run in runs]:
        raise SlingshotException(
            f"Run '{export_run_name}' (used as the 'export_run' for {label_studio_app_name}) was not found in "
            "'runs'. Please add it and try again."
        )


def _validate_source_mappings_are_unique(manifest: ProjectManifest) -> None:
    destinations = [source.remote_path for source in (manifest.sources or [])]
    if len(set(destinations)) != len(destinations):
        raise SlingshotException("Remote directories in source mappings must be unique.")
