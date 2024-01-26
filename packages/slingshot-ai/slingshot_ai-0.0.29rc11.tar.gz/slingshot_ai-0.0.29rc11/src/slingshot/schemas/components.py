from abc import abstractmethod
from typing import Any

from pydantic import ConfigDict, Field, field_validator, model_validator
from pydantic_core.core_schema import FieldValidationInfo

from slingshot.sdk import backend_schemas
from slingshot.sdk.graphql import fragments
from slingshot.shared.validation_warnings import SlingshotDeprecationWarning, record_validation_warning

from .common import ALPHANUMERIC_UNDERSCORE_HYPHEN_RE, SlingshotBaseModel
from .mounts import MountSpecUnion
from .utils import get_default_num_gpu, machine_size_to_machine_type_gpu_count, machine_type_gpu_count_to_machine_size


class AbstractComponentSpec(SlingshotBaseModel):
    """
    Base class for all component definitions, including runs, deployments, apps, and the specific app sub types.
    """

    model_config = ConfigDict(title="Component")

    name: str = Field(
        ..., title="Name", description="The name of the component.", pattern=ALPHANUMERIC_UNDERSCORE_HYPHEN_RE
    )
    machine_type: backend_schemas.MachineType = Field(
        ..., title="Machine type", description="The machine type to be used."
    )
    num_gpu: int | None = Field(
        None, title="Number of GPUs", description="The number of GPUs to use.", validate_default=True
    )

    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        """Returns a list of differences between this and another component spec."""
        diff = []
        name = existing.spec_name

        if self.name != name:
            diff.append(f"Name changed from '{name}' → '{self.name}'")

        existing_machine_type, existing_num_gpu = machine_size_to_machine_type_gpu_count(existing.machine_size)
        self_machine_type = self.machine_type
        self_num_gpu = self.num_gpu

        if self_machine_type != existing_machine_type:
            diff.append(f"Machine type changed from '{existing_machine_type}' → '{self_machine_type}'")
        if self_num_gpu != existing_num_gpu:
            diff.append(f"Number of GPUs changed from '{existing_num_gpu}' → '{self_num_gpu}'")
        return diff

    @abstractmethod
    def get_mounts(self) -> list[MountSpecUnion]:
        ...

    @classmethod
    def silent_default_machine_type(cls) -> backend_schemas.MachineType | None:
        return None

    @model_validator(mode='before')
    @classmethod
    def warn_on_missing_explicit_machine_type(cls, data: Any) -> Any:
        if 'machine_type' not in data or not data['machine_type']:
            silent_default = cls.silent_default_machine_type()
            if silent_default is not None:
                return {**data, 'machine_type': silent_default}
            else:
                default_machine_type = backend_schemas.MachineType.CPU_SMALL
                record_validation_warning(
                    SlingshotDeprecationWarning(
                        f"'machine_type' not set for '{data['name']}', defaulting to '{default_machine_type}'. "
                        + "Specifying machine_type will be required in upcoming versions of the CLI."
                    )
                )
                return {**data, 'machine_type': default_machine_type}
        else:
            return data

    @model_validator(mode='before')
    @classmethod
    def warn_on_use_of_machine_size(cls, data: dict[str, Any]) -> Any:
        if 'machine_size' in data:
            record_validation_warning(
                SlingshotDeprecationWarning(
                    "'machine_size' has been replaced with 'machine_type'. "
                    + "Use 'slingshot machines' to see available options"
                )
            )

        return data

    @field_validator("num_gpu", mode="before")
    @classmethod
    def validate_num_gpu(cls, v: int | None, info: FieldValidationInfo) -> int | None:
        """Validate that the number of GPUs is valid based on machine_type."""
        if "machine_type" not in info.data:
            # This means the user has input an invalid machine type, therefore we can't deduce the number of GPUs.
            return None
        machine_type: backend_schemas.MachineType = info.data["machine_type"]
        v = v if v is not None else get_default_num_gpu(machine_type)
        try:
            machine_type_gpu_count_to_machine_size(gpu_count=v, machine_type=machine_type)
        except ValueError as e:
            raise ValueError(f"Invalid number of GPUs ({v}) for machine type {machine_type}") from e
        return v
