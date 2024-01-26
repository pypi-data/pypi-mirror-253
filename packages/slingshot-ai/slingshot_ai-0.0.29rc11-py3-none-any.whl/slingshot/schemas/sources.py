from pathlib import Path, PurePath

from pydantic import Field, field_validator

from .common import SlingshotBaseModel


class SourceMapping(SlingshotBaseModel):
    """Represents an individual source mapping configuration, pointing a local directory to a remote one."""

    path: str = Field(..., title="Path", description="Mapping in the format <localdir>:<remotedir>.")
    exclude_paths: list[str] = Field(
        default_factory=list,
        alias="excludePaths",
        title="Exclude paths",
        description="A list of .gitignore style rules used to exclude source files.",
    )

    @property
    def local_path(self) -> Path:
        return Path(SourceMapping._split_path(self.path)[0])

    @property
    def remote_path(self) -> Path:
        return Path(SourceMapping._split_path(self.path)[1])

    @field_validator("path", mode='before')
    @classmethod
    def ensure_path_mapping_is_valid(cls, path: str) -> str:
        if not isinstance(path, str):
            raise ValueError("path must be a string")

        from_path_str, to_path_str = SourceMapping._split_path(path)

        PurePath(from_path_str)
        to_path = PurePath(to_path_str)

        if to_path.is_absolute():
            raise ValueError("Remote path must be relative")
        # NOTE: We prevent all usages of .. here for two reasons:
        # 1. So that we can prevent users from going above the working directory in a remote, as this won't work
        #    for the push/zip case
        # 2. So that we can compare remote paths without ambiguity, as we don't allow multiple mappings for the same
        #    remote directory (and we don't want to see both foo/../bar and bar)
        if ".." in to_path_str:
            raise ValueError("Remote path may not contain '..'")

        return path

    @staticmethod
    def _split_path(path_str: str) -> tuple[str, str]:
        # NOTE: Windows is a thing, don't just split on :, take the last occurance
        split_idx = path_str.rfind(":")
        if split_idx == -1:
            raise ValueError("Path must be in the format <localdir>:<remotedir>")
        return path_str[:split_idx], path_str[split_idx + 1 :]
