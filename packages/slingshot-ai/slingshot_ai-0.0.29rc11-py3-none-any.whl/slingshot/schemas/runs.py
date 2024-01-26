from pydantic import Field
from typing_extensions import override

from slingshot.sdk import backend_schemas
from slingshot.sdk.graphql import fragments

from .components import AbstractComponentSpec
from .mixins import ScriptBasedComponentMixin


class RunSpec(ScriptBasedComponentMixin, AbstractComponentSpec):
    resumable: bool | None = Field(
        None,
        title="Resumable",
        description="If set to true, this run is expected to be resumable, and may be scheduled to run on less reliable but cheaper machines",
    )
    max_restarts: int | None = Field(
        None,
        title="Max restarts",
        description="The total number of restarts allowed before this run fails. Note: This includes restarts both from your code crashing and infrastructure.",
    )
    enable_scratch_volume: bool | None = Field(
        None,
        title="Enable scratch volume",
        description="If true, a volume will automatically be created and made available in /mnt/scratch. The content of this volume will be available for the duration of the run (even across restarts) but will not be persisted.",
    )

    @override
    def diff(self, existing: fragments.ComponentSpec) -> list[str]:
        if existing.component_type != backend_schemas.ComponentType.RUN:
            raise ValueError(f"Cannot diff a run against a non-run.")

        diff = super().diff(existing)
        if self.resumable != existing.resumable:
            diff.append(f"Resumable changed from '{existing.resumable}' → '{self.resumable}'")
        if self.max_restarts != existing.max_restarts:
            diff.append(f"Max restarts changed from '{existing.max_restarts}' → '{self.max_restarts}'")
        if self.enable_scratch_volume != existing.enable_scratch_volume:
            diff.append(
                f"Enable scratch volume changed from '{existing.enable_scratch_volume}' → '{self.enable_scratch_volume}'"
            )

        return diff
