from __future__ import annotations

import typing

from . import backend_schemas

if typing.TYPE_CHECKING:
    from slingshot import SlingshotSDK


class WebPathUtil:
    def __init__(self, sdk: SlingshotSDK, slingshot_url: str):
        self._sdk = sdk
        self._slingshot_url = slingshot_url

    @property
    def homepage(self) -> str:
        return self._slingshot_url.rstrip("/")

    @typing.overload
    async def project(self, project: backend_schemas.Project) -> str:
        ...

    @typing.overload
    async def project(self, project: str) -> str:
        ...

    @typing.overload
    async def project(self) -> str:
        ...

    async def project(self, project: backend_schemas.Project | str | None = None) -> str:
        if project is None:
            project = await self._sdk._get_current_project_or_raise()
        if isinstance(project, str):
            project_id = project
        else:
            project_id = project.project_id
        return f"{self.homepage}/project/{project_id}/"

    @typing.overload
    async def code(self, source_code: backend_schemas.HasSourceCodeId) -> str:
        ...

    @typing.overload
    async def code(self, source_code: str) -> str:
        ...

    async def code(self, source_code: backend_schemas.HasSourceCodeId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(source_code, str):
            source_code_id = source_code
        else:
            source_code_id = source_code.source_code_id
        return f"{self.homepage}/project/{project.project_id}/code/{source_code_id}"

    @typing.overload
    async def blob_artifact(self, blob_artifact: backend_schemas.HasBlobArtifactId) -> str:
        ...

    @typing.overload
    async def blob_artifact(self, blob_artifact: str) -> str:
        ...

    async def blob_artifact(self, blob_artifact: backend_schemas.HasBlobArtifactId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(blob_artifact, str):
            blob_artifact_id = blob_artifact
        else:
            blob_artifact_id = blob_artifact.blob_artifact_id
        return f"{self.homepage}/project/{project.project_id}/artifacts/{blob_artifact_id}"

    @typing.overload
    async def app(self, component_spec: backend_schemas.HasComponentSpecId) -> str:
        ...

    @typing.overload
    async def app(self, component_spec: str) -> str:
        ...

    async def app(self, component_spec: backend_schemas.HasComponentSpecId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(component_spec, str):
            spec_id = component_spec
        else:
            spec_id = component_spec.spec_id
        return f"{self.homepage}/project/{project.project_id}/apps/{spec_id}"

    @typing.overload
    async def run(self, run: backend_schemas.HasRunId) -> str:
        ...

    @typing.overload
    async def run(self, run: str) -> str:
        ...

    async def run(self, run: backend_schemas.HasRunId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(run, str):
            run_id = run
        else:
            run_id = run.run_id
        return f"{self.homepage}/project/{project.project_id}/runs/{run_id}"

    @typing.overload
    async def deployment(self, deployment_spec: backend_schemas.HasComponentSpecId) -> str:
        ...

    @typing.overload
    async def deployment(self, deployment_spec: str) -> str:
        ...

    async def deployment(self, deployment_spec: backend_schemas.HasComponentSpecId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(deployment_spec, str):
            spec_id = deployment_spec
        else:
            spec_id = deployment_spec.spec_id
        return f"{self.homepage}/project/{project.project_id}/deployments/{spec_id}"

    @typing.overload
    async def environment(self, env: backend_schemas.HasExecutionEnvironmentSpecId) -> str:
        ...

    @typing.overload
    async def environment(self, env: str) -> str:
        ...

    async def environment(self, env: backend_schemas.HasExecutionEnvironmentSpecId | str) -> str:
        project = await self._sdk._get_current_project_or_raise()
        if isinstance(env, str):
            env_id = env
        else:
            env_id = env.execution_environment_spec_id
        return f"{self.homepage}/project/{project.project_id}/environments/{env_id}"
