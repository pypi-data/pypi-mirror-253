from __future__ import annotations

import json
import sys
import typing
from logging import getLogger
from typing import TYPE_CHECKING, Optional

from pydantic import ValidationError
from ruamel import yaml as r_yaml

from slingshot import schemas
from slingshot.cli.shared import create_empty_project_manifest, prompt_confirm
from slingshot.schemas import (
    HasAutoscalingParams,
    HasComponentConfig,
    HasProjectCredentials,
    ProjectManifest,
    requested_requirements_from_str,
)
from slingshot.schemas.utils import machine_size_to_machine_type_gpu_count, machine_type_gpu_count_to_machine_size
from slingshot.sdk import backend_schemas
from slingshot.sdk.config import client_settings
from slingshot.sdk.errors import SlingshotException, SlingshotFileNotFoundException
from slingshot.sdk.graphql import fragments
from slingshot.sdk.utils import console, recursive_enum_to_str
from slingshot.shared.config import load_slingshot_project_config
from slingshot.shared.utils import get_data_or_raise

if TYPE_CHECKING:
    from slingshot.sdk.slingshot_sdk import SlingshotSDK

    EnvSpecPlan = tuple[
        list[tuple[schemas.EnvironmentSpec, str]],
        list[tuple[schemas.EnvironmentSpec, fragments.ExecutionEnvironmentSpec]],
        list[fragments.ExecutionEnvironmentSpec],
    ]
    ComponentSpecPlan = tuple[
        list[schemas.AbstractComponentSpec],
        list[tuple[schemas.AbstractComponentSpec, str]],
        list[fragments.ComponentSpec],
    ]
else:
    EnvSpecPlan = tuple
    ComponentSpecPlan = tuple

logger = getLogger(__name__)
yaml = r_yaml.YAML()


def _convert_using_to_app_subtype(using: str) -> schemas.AppSubType:
    using = using.upper()
    using = using.replace("-", "_")
    return schemas.AppSubType(using)


class ApplyService:
    WAIT_FOR_ENV_POLL_INTERVAL = 2

    def __init__(self, sdk: "SlingshotSDK") -> None:
        if not (project := sdk.project):
            raise SlingshotException(
                "SDK has no project set.", cli="No project set. Please run 'slingshot init' or 'slingshot use'."
            )
        self._project = project
        self._sdk = sdk

    async def plan(self, config_: schemas.ProjectManifest | None = None) -> tuple[EnvSpecPlan, ComponentSpecPlan]:
        if not config_:
            config_ = load_slingshot_project_config()

        env_plan, _ = await self.plan_environments(config_)
        component_plan = await self.plan_components(config_)
        return env_plan, component_plan

    async def plan_component_spec(
        self, component_spec: schemas.AbstractComponentSpec, environments: dict[str, schemas.EnvironmentSpec]
    ) -> tuple[EnvSpecPlan, ComponentSpecPlan]:
        """
        Plans the changes to be applied to the provided component spec.
        """
        env_name: str | None = None
        env_spec: schemas.EnvironmentSpec | None = None
        if isinstance(component_spec, schemas.ComponentEnvironmentMixin):
            env_name = component_spec.environment
            env_spec = environments[env_name]

        existing_env_specs = await self._sdk.list_environments()
        existing_env = next(
            (env for env in existing_env_specs if env.execution_environment_spec_name == env_name), None
        )
        existing_envs = [existing_env] if existing_env else []
        yaml_envs = {env_name: env_spec} if env_name and env_spec else {}
        (env_specs_to_create, env_specs_to_update, _, _, env_change_msgs) = _diff_existing_env_yaml_specs(
            existing_envs, yaml_envs
        )

        component_type = _get_component_type(component_spec)
        assert self._sdk.project_id, "Project ID is not set"

        existing_spec = await self._sdk.api.get_component_spec_by_name(component_spec.name, self._sdk.project_id)
        (component_to_create, component_to_update, _, component_change_msgs) = _diff_existing_app_yaml_specs(
            [existing_spec] if existing_spec else [], [component_spec], component_type
        )

        all_change_msgs = env_change_msgs + component_change_msgs
        if all_change_msgs:
            console.print("\n".join(all_change_msgs))
        console.print("")
        return (env_specs_to_create, env_specs_to_update, []), (component_to_create, component_to_update, [])

    async def plan_components(self, config_: schemas.ProjectManifest) -> ComponentSpecPlan:
        existing_component_specs = await self._sdk.list_components()
        components_mapping: dict[schemas.ComponentType, typing.Sequence[schemas.AbstractComponentSpec]] = {
            schemas.ComponentType.RUN: config_.runs,
            schemas.ComponentType.DEPLOYMENT: config_.deployments,
        }

        component_specs_to_create = []
        component_specs_to_update = []
        component_specs_to_delete = []
        all_change_msgs = []

        # Check App Sub Types
        for app_sub_type in schemas.AppSubType:
            apps_from_sub_type = [
                app
                for app in config_.apps
                if isinstance(app, schemas.AbstractComponentSpec)
                and _convert_using_to_app_subtype(app.using) == app_sub_type
            ]
            (
                app_sub_type_specs_to_create,
                app_sub_type_component_specs_to_update,
                app_sub_type_component_specs_to_delete,
                app_sub_type_app_change_msgs,
            ) = _diff_existing_app_yaml_specs(
                existing_component_specs, apps_from_sub_type, schemas.ComponentType.APP, app_sub_type  # noqa
            )
            component_specs_to_create += app_sub_type_specs_to_create
            component_specs_to_update += app_sub_type_component_specs_to_update
            component_specs_to_delete += app_sub_type_component_specs_to_delete
            all_change_msgs += app_sub_type_app_change_msgs

        # Check Runs, Apps, Deployments
        for component_type, components in components_mapping.items():
            (
                component_type_specs_to_create,
                component_type_specs_to_update,
                component_type_specs_to_delete,
                component_type_change_msgs,
            ) = _diff_existing_app_yaml_specs(existing_component_specs, list(components), component_type)
            component_specs_to_create += component_type_specs_to_create
            component_specs_to_update += component_type_specs_to_update
            component_specs_to_delete += component_type_specs_to_delete
            all_change_msgs += component_type_change_msgs

        if all_change_msgs:
            console.print("\n".join(all_change_msgs))

        return component_specs_to_create, component_specs_to_update, component_specs_to_delete

    async def plan_environments(self, config_: schemas.ProjectManifest) -> tuple[EnvSpecPlan, set[str]]:
        existing_env_specs = await self._sdk.list_environments()
        (
            env_specs_to_create,
            env_specs_to_update,
            env_specs_to_delete,
            updated_spec_names,
            change_msgs,
        ) = _diff_existing_env_yaml_specs(existing_env_specs, config_.environments)
        if change_msgs:
            console.print("\n".join(change_msgs))
        return (env_specs_to_create, env_specs_to_update, env_specs_to_delete), updated_spec_names

    async def apply_env_specs(self, env_spec_plan: EnvSpecPlan) -> dict[str, str]:
        """
        Returns a dict mapping env spec names to env spec ids
        """
        env_specs_to_create, env_specs_to_update, env_specs_to_delete = env_spec_plan
        existing_specs = await self._sdk.list_environments()
        env_spec_name_to_id = {
            spec.execution_environment_spec_name: spec.execution_environment_spec_id for spec in existing_specs
        }

        has_env_updates = (len(env_specs_to_create) + len(env_specs_to_update) + len(env_specs_to_delete)) > 0
        if not has_env_updates:
            console.print("No changes detected to environments ✅ ")
            return env_spec_name_to_id

        for spec, spec_name in env_specs_to_create:
            try:
                new_env_spec = await self.create_env_spec(environment_name=spec_name, environment_spec=spec)
                env_spec_name_to_id[spec_name] = new_env_spec.execution_environment_spec_id
            except Exception as e:
                raise SlingshotException(f"Failed to create environment: {e}") from e

        for spec, existing_spec in env_specs_to_update:
            try:
                updated_env_spec = await self.update_env_spec(
                    environment_spec=spec, existing_execution_environment_spec=existing_spec
                )
                spec_id = updated_env_spec.execution_environment_spec_id
                env_spec_name_to_id[existing_spec.execution_environment_spec_name] = spec_id
            except Exception as e:
                raise SlingshotException(f"Failed to update environment: {e}") from e
        for env_spec_to_delete in env_specs_to_delete:
            try:
                await self.delete_env_spec(env_spec_to_delete)
            except Exception as e:
                raise SlingshotException(f"Failed to delete environment: {e}") from e
        return env_spec_name_to_id

    async def create_env_spec(
        self, environment_name: str, environment_spec: schemas.EnvironmentSpec
    ) -> fragments.ExecutionEnvironmentSpec:
        console.print(f"Creating environment '{environment_name}'...", end="")
        base_image = environment_spec.base_image
        requested_python_requirements = [requested_requirements_from_str(i) for i in environment_spec.python_packages]
        requested_apt_requirements = [schemas.RequestedAptPackage(name=p) for p in environment_spec.apt_packages]
        create_env_spec_resp = await self._sdk.create_environment(
            name=environment_name,
            base_image=base_image,
            requested_python_requirements=requested_python_requirements,
            requested_apt_requirements=requested_apt_requirements,
            post_install_command=environment_spec.post_install_command,
        )
        if create_env_spec_resp.error:
            raise SlingshotException(f"Failed to create environment: {create_env_spec_resp.error}")
        console.print("✅ ")

        create_env_spec = get_data_or_raise(create_env_spec_resp)
        env_spec = await self._sdk.get_environment(create_env_spec.execution_environment_spec_id)
        assert env_spec, "Environment was not created"
        return env_spec

    async def update_env_spec(
        self,
        environment_spec: schemas.EnvironmentSpec,
        existing_execution_environment_spec: fragments.ExecutionEnvironmentSpec,
    ) -> fragments.ExecutionEnvironmentSpec:
        environment_name = existing_execution_environment_spec.execution_environment_spec_name
        execution_environment_spec_id = existing_execution_environment_spec.execution_environment_spec_id
        console.print(f"Updating environment '{environment_name}'...", end="")
        base_image = environment_spec.base_image
        requested_python_requirements = [requested_requirements_from_str(i) for i in environment_spec.python_packages]
        requested_apt_requirements = [schemas.RequestedAptPackage(name=p) for p in environment_spec.apt_packages]
        await self._sdk.update_environment(
            name=environment_name,
            base_image=base_image,
            requested_python_requirements=requested_python_requirements,
            requested_apt_requirements=requested_apt_requirements,
            post_install_command=environment_spec.post_install_command,
        )
        console.print("✅ ")
        env_spec = await self._sdk.get_environment(execution_environment_spec_id)
        assert env_spec, "Environment was not updated"
        return env_spec

    async def delete_env_spec(self, env_spec: fragments.ExecutionEnvironmentSpec) -> None:
        console.print(f"Deleting environment '{env_spec.execution_environment_spec_name}'...", end="")
        await self._sdk.delete_environment(environment_id=env_spec.execution_environment_spec_id)
        console.print("✅ ")

    async def apply_component_specs(
        self, component_spec_plan: ComponentSpecPlan, env_spec_name_to_id: dict[str, str]
    ) -> None:
        component_specs_to_create, component_specs_to_update, component_specs_to_delete = component_spec_plan

        has_app_updates = (
            len(component_specs_to_create) + len(component_specs_to_update) + len(component_specs_to_delete)
        ) > 0
        if not has_app_updates:
            console.print("No changes detected to apps, runs, or deployments ✅ ")
            return

        # Note: temporary hack to make sure runs are created before everything else. This is needed because
        # Label Studio Apps now have references to run ids (which must exist before the app is created)
        run_specs_to_create = [
            component_spec
            for component_spec in component_specs_to_create
            if isinstance(component_spec, schemas.RunSpec)
        ]
        remaining_apps_to_create = [
            component_spec
            for component_spec in component_specs_to_create
            if not isinstance(component_spec, schemas.RunSpec)
        ]

        # Similarly, we need to delete runs last due to the foreign key constraint
        run_specs_to_delete = [
            component_spec
            for component_spec in component_specs_to_delete
            if component_spec.component_type == schemas.ComponentType.RUN
        ]
        remaining_apps_to_delete: list[fragments.ComponentSpec] = [
            component_spec
            for component_spec in component_specs_to_delete
            if component_spec.component_type != schemas.ComponentType.RUN
        ]

        for run_spec_to_create in run_specs_to_create:
            try:
                await self.create_component_spec(
                    component_spec=run_spec_to_create,
                    exec_env_spec_id=env_spec_name_to_id[run_spec_to_create.environment]
                    if run_spec_to_create.environment
                    else None,
                )
            except Exception as e:
                raise SlingshotException(f"Failed to create: {e}") from e

        for other_app_to_create in remaining_apps_to_create:
            try:
                # Note: if we're creating a Label Studio app, we need to fetch the import and export run ids first
                #  If/when we generalize Apps to own Runs, we should refactor this (or if this starts to get too messy)
                import_run_spec = None
                export_run_spec = None
                if isinstance(other_app_to_create, schemas.LabelStudioComponentSpec):
                    import_run_spec = await self._sdk.get_app(other_app_to_create.import_run)
                    export_run_spec = await self._sdk.get_app(other_app_to_create.export_run)
                    assert (
                        import_run_spec
                    ), f"Run for syncing to Label Studio '{other_app_to_create.import_run}' does not exist"
                    assert (
                        export_run_spec
                    ), f"Run for syncing from Label Studio '{other_app_to_create.export_run}' does not exist"
                env_name = getattr(other_app_to_create, "environment", None)
                env_spec_id = env_spec_name_to_id[env_name] if env_name else None
                _ = await self.create_component_spec(
                    component_spec=other_app_to_create,
                    exec_env_spec_id=env_spec_id,
                    import_run_spec=import_run_spec,
                    export_run_spec=export_run_spec,
                )
            except Exception as e:
                raise SlingshotException(f"Failed to create app: {e}") from e

        for app_to_update, app_to_update_id in component_specs_to_update:
            try:
                env_name = getattr(app_to_update, "environment", None)
                env_spec_id = env_spec_name_to_id[env_name] if env_name else None
                await self.update_component_spec(
                    component_spec=app_to_update,
                    existing_component_spec_id=app_to_update_id,
                    exec_env_spec_id=env_spec_id,
                )
            except Exception as e:
                raise SlingshotException(f"Failed to update app: {e}") from e
        for other_app_to_delete in remaining_apps_to_delete:
            try:
                await self.delete_component_spec(other_app_to_delete)
            except Exception as e:
                raise SlingshotException(f"Failed to delete: {e}") from e
        for spec in run_specs_to_delete:
            try:
                await self.delete_component_spec(spec)
            except Exception as e:
                raise SlingshotException(f"Failed to delete: {e}") from e

    async def create_component_spec(
        self,
        component_spec: schemas.AbstractComponentSpec,
        exec_env_spec_id: str | None = None,
        import_run_spec: backend_schemas.HasComponentSpecId | None = None,
        export_run_spec: backend_schemas.HasComponentSpecId | None = None,
    ) -> backend_schemas.HasComponentSpecId:
        console.print(f"Creating '{component_spec.name}'...", end="")
        run_spec: schemas.RunSpec | None = component_spec if isinstance(component_spec, schemas.RunSpec) else None
        component_type = _get_component_type(component_spec)
        app_sub_type = _get_app_sub_type(component_spec)
        deployment_sub_type = _get_deployment_sub_type(component_spec)
        machine_size = machine_type_gpu_count_to_machine_size(component_spec.machine_type, component_spec.num_gpu)
        component_spec_id_response = await self._sdk.create_component(
            name=component_spec.name,
            command=component_spec.cmd if hasattr(component_spec, "cmd") else None,
            component_type=component_type,
            app_sub_type=app_sub_type,
            deployment_sub_type=deployment_sub_type,
            exec_env_spec_id=exec_env_spec_id,
            machine_size=machine_size,
            mounts=component_spec.get_mounts(),
            attach_project_credentials=(
                component_spec.attach_project_credentials
                if isinstance(component_spec, HasProjectCredentials)
                else False
            ),
            config_variables=(
                component_spec.config_variables if isinstance(component_spec, HasComponentConfig) else None
            ),
            app_port=component_spec.port if hasattr(component_spec, "port") else None,
            import_run_spec_id=import_run_spec.spec_id if import_run_spec else None,
            export_run_spec_id=export_run_spec.spec_id if export_run_spec else None,
            min_replicas=component_spec.min_replicas if isinstance(component_spec, HasAutoscalingParams) else None,
            max_replicas=component_spec.max_replicas if isinstance(component_spec, HasAutoscalingParams) else None,
            resumable=run_spec.resumable if run_spec else None,
            max_restarts=run_spec.max_restarts if run_spec else None,
            enable_scratch_volume=run_spec.enable_scratch_volume if run_spec else None,
        )
        spec_id = get_data_or_raise(component_spec_id_response)
        console.print("✅")
        return spec_id

    async def update_component_spec(
        self,
        component_spec: schemas.AbstractComponentSpec,
        existing_component_spec_id: str,
        exec_env_spec_id: str | None = None,
        import_run_spec: backend_schemas.HasComponentSpecId | None = None,
        export_run_spec: backend_schemas.HasComponentSpecId | None = None,
    ) -> None:
        component_type = _get_component_type(component_spec)
        run_spec: schemas.RunSpec | None = component_spec if isinstance(component_spec, schemas.RunSpec) else None
        app_sub_type = _get_app_sub_type(component_spec)
        spec_display_name = _get_spec_display_name(component_type, app_sub_type)
        console.print(f"Updating {spec_display_name} '{component_spec.name}'...", end="")
        machine_size = machine_type_gpu_count_to_machine_size(component_spec.machine_type, component_spec.num_gpu)
        await self._sdk.update_component(
            spec_id=existing_component_spec_id,
            command=component_spec.cmd if hasattr(component_spec, "cmd") else None,
            env_spec_id=exec_env_spec_id,
            machine_size=machine_size,
            config_variables=component_spec.config_variables
            if isinstance(component_spec, HasComponentConfig)
            else None,
            mounts=component_spec.get_mounts(),
            attach_project_credentials=(
                component_spec.attach_project_credentials
                if isinstance(component_spec, HasProjectCredentials)
                else False
            ),
            app_port=component_spec.port if hasattr(component_spec, "port") else None,
            batch_size=component_spec.batch_size if hasattr(component_spec, "batch_size") else None,
            batch_interval=component_spec.batch_interval if hasattr(component_spec, "batch_interval") else None,
            import_run_spec_id=import_run_spec.spec_id if import_run_spec else None,
            export_run_spec_id=export_run_spec.spec_id if export_run_spec else None,
            min_replicas=component_spec.min_replicas if isinstance(component_spec, HasAutoscalingParams) else None,
            max_replicas=component_spec.max_replicas if isinstance(component_spec, HasAutoscalingParams) else None,
            resumable=run_spec.resumable if run_spec else None,
            max_restarts=run_spec.max_restarts if run_spec else None,
            enable_scratch_volume=run_spec.enable_scratch_volume if run_spec else None,
        )
        console.print("✅ ")

    async def delete_component_spec(self, component_spec: fragments.ComponentSpec) -> None:
        console.print(
            f"Deleting {component_spec.friendly_component_type} '{component_spec.spec_name}' from the remote project manifest...",
            end="",
        )
        await self._sdk.delete_app(spec_id=component_spec.spec_id)
        console.print("✅ ")

    async def apply(self, force: bool = False) -> bool:
        """
        Plan and apply changes from your local Slingshot YAML.

        Returns if any changes were applied.
        """
        local_manifest = load_slingshot_project_config(force_reload=True, silence_warnings=True)
        env_spec_plan, component_spec_plan = await self.plan(config_=local_manifest)
        if any(env_spec_plan) or any(component_spec_plan):
            if force or prompt_confirm("Do you want to apply these changes?", default=True):
                console.print(f"Applying 'slingshot.yaml' for project '{self._project.project_id}'.")
                env_spec_name_to_id = await self.apply_env_specs(env_spec_plan=env_spec_plan)
                await self.apply_component_specs(
                    component_spec_plan=component_spec_plan, env_spec_name_to_id=env_spec_name_to_id
                )
                await self.restart_updated_apps(env_spec_plan=env_spec_plan, component_spec_plan=component_spec_plan)
                return True
        return False

    async def apply_component(self, *, component_type: schemas.ComponentType, component_name: str) -> bool:
        """
        Plan and apply changes to an individual component by name. Raises and error if the component does not exist in
        the local manifest.

        Returns if any changes were applied.
        """
        local_manifest = load_slingshot_project_config(force_reload=True, silence_warnings=True)
        local_components: list[typing.Any]  # TODO: type hack to avoid mypy error around spec types
        if component_type == schemas.ComponentType.RUN:
            local_components = local_manifest.runs
        elif component_type == schemas.ComponentType.APP:
            local_components = local_manifest.apps
        elif component_type == schemas.ComponentType.DEPLOYMENT:
            local_components = local_manifest.deployments
        else:
            raise AssertionError(f"Unrecognized component type: {component_type}")

        component = next((c for c in local_components if c.name == component_name), None)
        if not component:
            raise SlingshotException(f"Component '{component_name}' not found in local manifest.")

        env_spec_plan, component_spec_plan = await self.plan_component_spec(
            component_spec=component, environments=local_manifest.environments
        )
        if any(env_spec_plan) or any(component_spec_plan):
            spec_display_name = _get_spec_display_name(component_type, _get_app_sub_type(component))
            if prompt_confirm(
                f"Changes detected to {spec_display_name} '{component_name}' in your 'slingshot.yaml'.\nDo you want to apply these changes?",
                default=True,
            ):
                env_spec_name_to_id = await self.apply_env_specs(env_spec_plan=env_spec_plan)
                await self.apply_component_specs(
                    component_spec_plan=component_spec_plan, env_spec_name_to_id=env_spec_name_to_id
                )
                return True
        return False

    async def restart_updated_apps(self, env_spec_plan: EnvSpecPlan, component_spec_plan: ComponentSpecPlan) -> None:
        _, component_specs_to_update, _ = component_spec_plan

        # We only want to restart deployments and custom apps
        apps_or_deployments_to_restart = [
            (component_spec, component_type)
            for component_spec, _ in component_specs_to_update
            if (component_type := _get_component_type(component_spec))
            in {schemas.ComponentType.DEPLOYMENT, schemas.ComponentType.APP}
        ]
        # TODO: also restart apps and deployments if their envs changed

        for component_spec, component_type in apps_or_deployments_to_restart:
            match component_type:
                case schemas.ComponentType.DEPLOYMENT:
                    deployment_spec = await self._sdk.get_deployment(deployment_name=component_spec.name)
                    deployment_is_active = (
                        deployment_spec
                        and deployment_spec.deployment_status
                        and deployment_spec.deployment_status.is_active
                    )
                    if not deployment_is_active:
                        continue
                    if prompt_confirm(f"Do you want to restart deployment '{component_spec.name}'?", default=False):
                        console.print("Restarting deployment...", end="")
                        await self._sdk.start_deployment(deployment_name=component_spec.name)
                        console.print("✅")

                case schemas.ComponentType.APP:
                    app_spec = await self._sdk.get_app(app_name=component_spec.name)
                    app_is_active = app_spec and app_spec.app_instance_status and app_spec.app_instance_status.is_active
                    if not app_is_active:
                        continue
                    if prompt_confirm(f"Do you want to restart app '{component_spec.name}'?", default=False):
                        console.print("Restarting app...", end="")
                        await self._sdk.start_app(app_name=component_spec.name)
                        console.print("✅")

    async def export(self, should_print: bool = False) -> typing.Any:
        """
        Export the current state of your project in YAML format. Returns the remote project manifest.
        """
        remote_manifest = await _safe_load_remote_project_manifest(self._sdk, raise_on_error=True)
        manifest_obj = recursive_enum_to_str(remote_manifest.model_dump())
        if should_print:
            console.print("[cyan]Project YAML configuration:[/cyan]")
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(manifest_obj, sys.stdout)
        return manifest_obj


def _get_component_type(spec: schemas.AbstractComponentSpec) -> schemas.ComponentType:
    if isinstance(spec, schemas.RunSpec):
        return schemas.ComponentType.RUN
    elif isinstance(spec, schemas.AbstractDeploymentSpec):
        return schemas.ComponentType.DEPLOYMENT
    elif isinstance(spec, schemas.AbstractAppSpec):
        return schemas.ComponentType.APP
    else:
        raise AssertionError("Unrecognized component type " + repr(spec))


def _get_app_sub_type(spec: schemas.AbstractComponentSpec) -> backend_schemas.AppSubType | None:
    if isinstance(spec, schemas.AbstractAppSpec):
        if isinstance(spec, schemas.WebappComponentSpec):
            return backend_schemas.AppSubType.WEBAPP
        elif isinstance(spec, schemas.SessionComponentSpec):
            return backend_schemas.AppSubType.SESSION
        elif isinstance(spec, schemas.RedisComponentSpec):
            return backend_schemas.AppSubType.REDIS
        elif isinstance(spec, schemas.LabelStudioComponentSpec):
            return backend_schemas.AppSubType.LABEL_STUDIO
        else:
            raise AssertionError("Unrecognized app type: " + repr(spec))
    else:
        return None


def _get_deployment_sub_type(spec: schemas.AbstractComponentSpec) -> backend_schemas.DeploymentSubType | None:
    if isinstance(spec, schemas.AbstractDeploymentSpec):
        if isinstance(spec, schemas.CustomDeploymentSpec):
            return backend_schemas.DeploymentSubType.CUSTOM
        if isinstance(spec, schemas.StreamingTextDeploymentSpec):
            return backend_schemas.DeploymentSubType.STREAMING_TEXT
        else:
            raise AssertionError("Unrecognized deployment type: " + repr(spec))
    else:
        return None


def _diff_existing_env_yaml_specs(
    existing_env_specs: list[fragments.ExecutionEnvironmentSpec], yaml_env_specs: dict[str, schemas.EnvironmentSpec]
) -> tuple[
    list[tuple[schemas.EnvironmentSpec, str]],  # tuple of spec, name
    list[tuple[schemas.EnvironmentSpec, fragments.ExecutionEnvironmentSpec]],  # tuple of spec, existing spec to update
    list[fragments.ExecutionEnvironmentSpec],  # existing specs to delete
    set[str],  # updated spec names
    list[str],  # change messages
]:
    env_specs_to_create: list[tuple[schemas.EnvironmentSpec, str]] = []
    env_specs_to_update: list[tuple[schemas.EnvironmentSpec, fragments.ExecutionEnvironmentSpec]] = []
    env_specs_to_delete: list[fragments.ExecutionEnvironmentSpec] = []

    existing_env_names = {spec.execution_environment_spec_name for spec in existing_env_specs}
    existing_env_name_to_spec = {spec.execution_environment_spec_name: spec for spec in existing_env_specs}
    yaml_env_names = {spec_name for spec_name in yaml_env_specs.keys()}

    updated_spec_names: set[str] = set()
    change_msgs: list[str] = []
    for spec_name, env_spec in yaml_env_specs.items():
        if spec_name not in existing_env_names:
            change_msgs.append(f"[green](+)[/green] environment '{spec_name}'")
            env_specs_to_create.append((env_spec, spec_name))
            continue

        _change_msgs: list[str] = []
        existing_env_spec = existing_env_name_to_spec[spec_name]
        if diff := env_spec.diff(existing_env_spec):
            _change_msgs.extend(f"\t- {i}" for i in diff)
        if _change_msgs:
            change_msgs.append(f"Detected [yellow]changes[/yellow] to environment '{spec_name}'")
            change_msgs.extend(_change_msgs)
            updated_spec_names.add(spec_name)
            env_specs_to_update.append((env_spec, existing_env_spec))

    for existing_spec in existing_env_specs:
        if existing_spec.execution_environment_spec_name not in yaml_env_names:
            logger.debug(
                f"Detected environment '{existing_spec.execution_environment_spec_name}' has been [red]deleted[/red]"
            )
            logger.debug(f"\t- Environment will be [red]deleted[/red]")
            env_specs_to_delete.append(existing_spec)

    return env_specs_to_create, env_specs_to_update, env_specs_to_delete, updated_spec_names, change_msgs


def _diff_existing_app_yaml_specs(
    all_existing_component_specs: list[fragments.ComponentSpec],
    yaml_component_specs: typing.Sequence[schemas.AbstractComponentSpec],
    component_type: schemas.ComponentType,
    app_sub_type: schemas.AppSubType | None = None,
) -> tuple[
    list[schemas.AbstractComponentSpec],
    list[tuple[schemas.AbstractComponentSpec, str]],
    list[fragments.ComponentSpec],
    list[str],
]:
    spec_display_name = _get_spec_display_name(component_type, app_sub_type)
    component_specs_to_create: list[schemas.AbstractComponentSpec] = []
    component_specs_to_update: list[tuple[schemas.AbstractComponentSpec, str]] = []
    component_specs_to_delete: list[fragments.ComponentSpec] = []

    existing_component_specs = [spec for spec in all_existing_component_specs if spec.component_type == component_type]
    existing_spec_name_to_spec: dict[str, fragments.ComponentSpec] = {
        component_spec.spec_name: component_spec for component_spec in existing_component_specs
    }
    yaml_component_spec_names = {component_spec.name for component_spec in yaml_component_specs}

    change_msgs: list[str] = []
    for component_spec in yaml_component_specs:
        if component_spec.name not in existing_spec_name_to_spec:
            change_msgs.append(f"[green](+)[/green] {spec_display_name} '{component_spec.name}'")
            component_specs_to_create.append(component_spec)
            continue

        existing_component_spec = existing_spec_name_to_spec[component_spec.name]
        _change_msgs: list[str] = []
        if component_spec_diff := component_spec.diff(existing_component_spec):
            _change_msgs.extend(f"\t- {i}" for i in component_spec_diff)
        if _change_msgs:
            change_msgs.append(f"[yellow]Changes[/yellow] to {spec_display_name} '{component_spec.name}'")
            change_msgs.extend(_change_msgs)

        # Only update if there are changes to the component spec itself, not just the environment
        if len(component_spec_diff) > 0:
            component_specs_to_update.append((component_spec, existing_component_spec.spec_id))

    for existing_component_spec in existing_component_specs:
        if existing_component_spec.spec_name not in yaml_component_spec_names and (
            _normalize_app_sub_type(existing_component_spec) == app_sub_type
        ):
            console.print(f"[red](-)[/red] {spec_display_name} '{existing_component_spec.spec_name}'")
            component_specs_to_delete.append(existing_component_spec)

    return component_specs_to_create, component_specs_to_update, component_specs_to_delete, change_msgs


def _normalize_app_sub_type(app: fragments.ComponentSpec) -> Optional[schemas.AppSubType]:
    """
    Ensures that an app always has an app sub type type. Prior to Aug 2023, apps without a
    'using' configured (without a sub type) were treated by default as web apps.
    """
    if app.component_type == schemas.ComponentType.APP and app.app_sub_type is None:
        return schemas.AppSubType.WEBAPP
    return app.app_sub_type


async def _safe_load_remote_project_manifest(sdk: "SlingshotSDK", raise_on_error: bool) -> schemas.ProjectManifest:
    try:
        return await _remote_project_manifest(sdk)
    # TODO: wrap ValidationError that we throw as a subtype of a SlingshotException?
    except (SlingshotException, ValidationError) as e:
        error_msg = e.cli if isinstance(e, SlingshotException) else str(e)
        if raise_on_error:
            raise SlingshotException(
                f"Error reading the remote slingshot manifest: {error_msg}\n"
                f"Try force applying with `slingshot apply -f`, or contact Slingshot support if this issue persists."
            )
        console.print(f"[yellow]Warning[/yellow]: {error_msg}")
        return ProjectManifest()  # Return an empty manifest if we failed to load and don't want to raise


async def _remote_project_manifest(sdk: "SlingshotSDK") -> schemas.ProjectManifest:
    # Build environment specs
    existing_env_specs = await sdk.list_environments()
    env_specs_by_name = {}
    for env_spec in existing_env_specs:
        assert env_spec.environment_instances, "Environment spec has no instances"
        env_instance = env_spec.environment_instances[0]
        parsed_env_spec = schemas.EnvironmentSpec(
            # NOTE: No support for specific CPU/GPU base images in the schema, these will be the same if a custom
            # image is used, so we pick one of them.
            base_image=env_instance.cpu_base_image if env_instance.is_custom_base_image else None,
            python_packages=[
                str(backend_schemas.RequestedRequirement.model_validate(i))
                for i in env_instance.requested_python_requirements
            ],
            apt_packages=[
                schemas.RequestedAptPackage.model_validate(i).name for i in env_instance.requested_apt_packages
            ],
            post_install_command=env_instance.post_install_command,
        )
        env_specs_by_name[env_spec.execution_environment_spec_name] = parsed_env_spec

    # Build app specs
    component_specs: list[schemas.AbstractComponentSpec] = []
    existing_component_specs = await sdk.list_components()
    for spec in existing_component_specs:
        name = spec.spec_name
        existing_env_spec = spec.execution_environment_spec
        environment = existing_env_spec.execution_environment_spec_name if existing_env_spec else None
        config_variables = json.loads(spec.config_variables) if spec.config_variables else {}
        port = spec.app_port
        attach_project_credentials = spec.service_account
        cmd = spec.command
        machine_type, num_gpu = machine_size_to_machine_type_gpu_count(spec.machine_size)
        mounts = [schemas.remote_mount_spec_to_local(ms) for ms in spec.mount_specs]
        if spec.component_type == schemas.ComponentType.APP and (
            spec.app_sub_type is None or spec.app_sub_type == schemas.AppSubType.WEBAPP
        ):
            assert environment, f"Custom app '{name}' has no environment"
            assert cmd, f"Custom app '{name}' has no command"
            component_specs.append(
                schemas.WebappComponentSpec(
                    name=name,
                    environment=environment,
                    machine_type=machine_type,
                    num_gpu=num_gpu,
                    config_variables=config_variables,
                    port=port,
                    attach_project_credentials=attach_project_credentials,
                    cmd=cmd,
                    using="webapp",
                    mounts=mounts,
                )
            )
        elif spec.component_type == schemas.ComponentType.APP and spec.app_sub_type == schemas.AppSubType.SESSION:
            assert environment, f"Session app '{name}' has no environment"
            component_specs.append(
                schemas.SessionComponentSpec(
                    using="session",
                    name=name,
                    environment=environment,
                    machine_type=machine_type,
                    num_gpu=num_gpu,
                    mounts=mounts,
                )
            )
        elif spec.component_type == schemas.ComponentType.APP and spec.app_sub_type == schemas.AppSubType.REDIS:
            component_specs.append(
                schemas.RedisComponentSpec(name=name, machine_type=machine_type, num_gpu=num_gpu, using="redis")
            )
        elif spec.component_type == schemas.ComponentType.APP and spec.app_sub_type == schemas.AppSubType.LABEL_STUDIO:
            component_specs.append(
                schemas.LabelStudioComponentSpec(
                    name=name, machine_type=machine_type, num_gpu=num_gpu, using="label-studio"
                )
            )
        elif spec.component_type == schemas.ComponentType.RUN:
            assert environment, f"Run app '{name}' has no environment"
            assert cmd, f"Run app '{name}' has no command"
            component_specs.append(
                schemas.RunSpec(
                    name=name,
                    environment=environment,
                    machine_type=machine_type,
                    num_gpu=num_gpu,
                    config_variables=config_variables,
                    attach_project_credentials=attach_project_credentials,
                    cmd=cmd,
                    mounts=mounts,
                    resumable=spec.resumable,
                    max_restarts=spec.max_restarts,
                    enable_scratch_volume=spec.enable_scratch_volume,
                )
            )
        elif spec.component_type == schemas.ComponentType.DEPLOYMENT:
            if spec.deployment_sub_type is None or spec.deployment_sub_type == backend_schemas.DeploymentSubType.CUSTOM:
                assert environment, f"Deployment '{name}' has no environment"
                assert cmd, f"Deployment '{name}' has no command"
                component_specs.append(
                    schemas.CustomDeploymentSpec.new(
                        name=name,
                        environment=environment,
                        machine_type=machine_type,
                        num_gpu=num_gpu,
                        config_variables=config_variables,
                        attach_project_credentials=attach_project_credentials,
                        cmd=cmd,
                        mounts=mounts,
                        min_replicas=spec.min_replicas,
                        max_replicas=spec.max_replicas,
                    )
                )
            elif spec.deployment_sub_type == backend_schemas.DeploymentSubType.STREAMING_TEXT:
                component_specs.append(
                    schemas.StreamingTextDeploymentSpec.new(
                        name=name,
                        machine_type=machine_type,
                        num_gpu=num_gpu,
                        mounts=mounts,
                        min_replicas=spec.min_replicas,
                        max_replicas=spec.max_replicas,
                    )
                )
            else:
                raise ValueError(f"Unknown deployment type {spec.deployment_sub_type}")
        else:
            raise ValueError(f"Unknown component type {spec.component_type}")

    # Some cheeky type opt-outs here, mypy doesn't know that the abstract base class and the union of concrete classes
    # is the same thing ...
    return schemas.ProjectManifest(
        environments=env_specs_by_name,
        apps=[component for component in component_specs if isinstance(component, schemas.AbstractAppSpec)],  # type: ignore
        runs=[component for component in component_specs if isinstance(component, schemas.RunSpec)],
        deployments=[
            component for component in component_specs if isinstance(component, schemas.AbstractDeploymentSpec)  # type: ignore
        ],
    )


def _load_local_manifest(create_empty: bool) -> schemas.ProjectManifest:
    """Load the current local manifest, or create an empty one if it doesn't exist."""
    if create_empty:
        try:
            current_manifest = load_slingshot_project_config()  # Reload local, in case it was changed
        except SlingshotFileNotFoundException:
            create_empty_project_manifest(client_settings.slingshot_config_path)
            current_manifest = load_slingshot_project_config()  # Reload local, which is now an empty manifest.
    else:
        current_manifest = load_slingshot_project_config()
    return current_manifest


def _get_spec_display_name(component_type: schemas.ComponentType, app_sub_type: schemas.AppSubType | None) -> str:
    """Return the display name for the component type and sub type."""
    match component_type:
        case schemas.ComponentType.APP:
            match app_sub_type:
                case schemas.AppSubType.WEBAPP:
                    return "web app"
                case schemas.AppSubType.SESSION:
                    return "session"
                case schemas.AppSubType.REDIS:
                    return "redis"
                case schemas.AppSubType.LABEL_STUDIO:
                    return "label studio"
                case _:
                    return "app"
        case schemas.ComponentType.RUN:
            return "run"
        case schemas.ComponentType.DEPLOYMENT:
            return "deployment"
        case _:
            raise ValueError(f"Unknown component type {component_type}")
