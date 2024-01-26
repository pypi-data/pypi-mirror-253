from typing import Literal, Optional

from pydantic import ConfigDict, Field, TypeAdapter, field_validator

from slingshot.sdk import backend_schemas
from slingshot.sdk.graphql import fragments

from .common import SlingshotBaseModel
from .utils import requested_requirements_from_str


class EnvironmentSpec(SlingshotBaseModel):
    model_config = ConfigDict(
        title="Environment",
        json_schema_extra={
            "example": {"python_version": "3.10", "python_packages": ["numpy", "pandas", "torch==2.0.1"]}
        },
    )
    base_image: Optional[str] = Field(
        None,
        title="Base image",
        description="Base docker image to use to build the environment",
        pattern="^([\w\-_]+(\.[\w\-_]+)*(:\d+)?)(/[a-z0-9._-]+)*(:([\w\d.\-_]{1,127}))?$",
    )
    python_version: Literal["3.10"] = Field("3.10", title="Python version")
    python_packages: list[str] = Field(
        default_factory=list,
        title="Python packages",
        description=f"List of Python packages to install in the environment.",
    )
    post_install_command: str = Field(
        "",
        title="Post-install command",
        description="Custom command to run after all packages have been installed. Skipped if not specified.",
    )
    apt_packages: list[str] = Field(
        default_factory=list, title="APT packages", description=f"List of APT packages to install"
    )

    # All python packages can be converted to RequestedRequirement
    @field_validator("python_packages")
    @classmethod
    def convert_python_packages(cls, v: list[str]) -> list[str]:
        for i in v:
            try:
                requested_requirements_from_str(i)
            except ValueError as e:
                raise ValueError(f"Error occurred while trying to parse python packages") from e
        return v

    def diff(self, existing: fragments.ExecutionEnvironmentSpec) -> list[str]:
        """Returns a list of differences between this and another environment."""
        diff = []

        current_python_packages = [requested_requirements_from_str(pkg) for pkg in self.python_packages]
        current_apt_packages = [backend_schemas.RequestedAptPackage(name=pkg) for pkg in self.apt_packages]
        assert existing.environment_instances, "Environment spec has no instances"
        existing_env_instance = existing.environment_instances[0]
        existing_custom_base_image = (
            existing_env_instance.cpu_base_image if existing_env_instance.is_custom_base_image else None
        )
        if existing_custom_base_image != self.base_image:
            diff.append(f"Base image: {existing_custom_base_image} → {self.base_image}")
        existing_python_packages = TypeAdapter(list[backend_schemas.RequestedRequirement]).validate_python(
            existing_env_instance.requested_python_requirements
        )
        existing_apt_packages = TypeAdapter(list[backend_schemas.RequestedAptPackage]).validate_python(
            existing_env_instance.requested_apt_packages
        )
        existing_post_install_command = existing_env_instance.post_install_command

        if existing_post_install_command != self.post_install_command:
            existing_post_install_command_repr = existing_post_install_command.replace("\n", "\\n")
            new_post_install_command_repr = self.post_install_command.replace("\n", "\\n")
            diff.append(f"Post-install command: {existing_post_install_command_repr} → {new_post_install_command_repr}")

        python_package_diffs = self._diff_python_requirements(current_python_packages, existing_python_packages)
        if python_package_diffs:
            diff.append(f"Python packages changed")
            diff.extend(python_package_diffs)

        apt_package_diffs = self._diff_apt_packages(current_apt_packages, existing_apt_packages)
        if apt_package_diffs:
            diff.append(f"APT packages changed")
            diff.extend(apt_package_diffs)

        return diff

    @staticmethod
    def _diff_python_requirements(
        current: list[backend_schemas.RequestedRequirement], existing: list[backend_schemas.RequestedRequirement]
    ) -> list[str]:
        diff = []
        for req in current:
            if req not in existing:
                diff.append(f"  [green]+[/green] {str(req)}")
        for req in existing:
            if req not in current:
                diff.append(f"  [red]-[/red] {str(req)}")
        return diff

    @staticmethod
    def _diff_apt_packages(
        current: list[backend_schemas.RequestedAptPackage], existing: list[backend_schemas.RequestedAptPackage]
    ) -> list[str]:
        diff = []
        for req in current:
            if req not in existing:
                diff.append(f"  [green]+[/green] {req.name}")
        for req in existing:
            if req not in current:
                diff.append(f"  [red]-[/red] {req.name}")
        return diff
