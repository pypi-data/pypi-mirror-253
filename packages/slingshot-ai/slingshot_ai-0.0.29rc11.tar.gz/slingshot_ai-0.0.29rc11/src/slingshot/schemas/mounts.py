from typing import Annotated, Literal, Union

from pydantic import Field, field_validator
from typing_extensions import Self, override

from slingshot.sdk.errors import SlingshotException
from slingshot.sdk.graphql import fragments

from .common import SlingshotBaseModel
from .utils import has_path_ending_in_filename


class BaseMountSpec(SlingshotBaseModel):
    mode: str = Field(..., title="Mode", description="The mode to use for the mount.")
    path: str = Field(..., title="Path", description="The path to mount into the environment.", pattern=r'/mnt/[\w-]+')

    @field_validator('path', mode='after')
    @classmethod
    def fail_on_mount_paths_that_look_like_filenames(cls, path: str) -> str:
        if has_path_ending_in_filename(path):
            # TODO: raise custom error type instead of ValueError here and in other places so we can handle explicitly
            raise ValueError(
                f"The specified mount path '{path}' appears to be a filename. "
                + "Mounts paths must refer to directories, rather than individual files"
            )
        return path

    def diff(self, other: "BaseMountSpec") -> list[str]:
        what_changed = []
        if self.mode != other.mode:
            what_changed.append(f"mode: {other.mode} → {self.mode}")
        if self.path != other.path:
            what_changed.append(f"path: {other.path} → {self.path}")
        return what_changed


class MountSelector(SlingshotBaseModel):
    name: str = Field(..., title="Name", description="The name of the artifact to download.")
    tag: str | None = Field('latest', title="Tag", description="The tag of the artifact.")
    project: str | None = Field(
        None,
        title="Project",
        description="The id of a project to download an artifact from, only required when accessing artifacts from other projects",
    )

    def diff(self, other: Self) -> list[str]:
        what_changed = []
        if self.name != other.name:
            what_changed.append(f"name: {other.name} → {self.name}")
        if self.tag != other.tag and self.tag and other.tag:
            what_changed.append(f"tag: {other.tag} → {self.tag}")
        if self.project != other.project and self.tag and self.project is not None and other.project is not None:
            what_changed.append(f"project: {other.project} → {self.project}")
        return what_changed


class MountTarget(SlingshotBaseModel):
    name: str = Field(..., title="Name", description="The name of the artifact to upload.")
    tag: str | None = Field(None, title="Tag", description="The tag(s) to apply to the artifact, comma separated.")

    @property
    def tags(self) -> list[str]:
        """Gets the tags as a list, sorted alphabetically to ensure a canonical representation."""
        raw_tags = self.tag.split(',') if self.tag else []
        return sorted(_filter_empty_tags(raw_tags))

    def diff(self, other: Self) -> list[str]:
        what_changed = []
        if self.name != other.name:
            what_changed.append(f"name: {other.name} → {self.name}")
        if self.tags != other.tags and self.tag:
            what_changed.append(f"tag(s): {','.join(other.tags) or 'None'} → {','.join(self.tags) or 'None'}")
        return what_changed


class DownloadMountSpec(BaseMountSpec):
    mode: Literal["DOWNLOAD"] = Field(..., title="Mode", description="The mode to use for the mount.")
    selector: MountSelector = Field(..., title="Selector", description="The artifact selector.")

    @override
    def diff(self, other: BaseMountSpec) -> list[str]:
        d = super().diff(other)
        if isinstance(other, DownloadMountSpec):
            d.extend(self.selector.diff(other.selector))
        return d


class DownloadS3BucketMountSpec(BaseMountSpec):
    mode: Literal["DOWNLOAD_S3"] = Field(..., title="Mode", description="The mode to use for the mount.")
    name: str = Field(..., title="Name", description="The name of the mount.")
    s3_bucket_uri: str = Field(..., title="S3 Bucket URI", description="Which S3 URI to use for the mount.")

    @override
    def diff(self, other: BaseMountSpec) -> list[str]:
        d = super().diff(other)
        if isinstance(other, DownloadS3BucketMountSpec):
            if other.name != self.name:
                d.append(f"name: {other.name} → {self.name}")
            if other.s3_bucket_uri != self.s3_bucket_uri:
                d.append(f"s3_bucket_uri: {other.s3_bucket_uri} → {self.s3_bucket_uri}")
        return d


class UploadMountSpec(BaseMountSpec):
    mode: Literal["UPLOAD"] = Field(..., title="Mode", description="The mode to use for the mount.")
    target: MountTarget = Field(..., title="Target", description="The artifact target.")

    @override
    def diff(self, other: BaseMountSpec) -> list[str]:
        d = super().diff(other)
        if isinstance(other, UploadMountSpec):
            d.extend(self.target.diff(other.target))
        return d


class UploadS3BucketMountSpec(BaseMountSpec):
    mode: Literal["UPLOAD_S3"] = Field(..., title="Mode", description="The mode to use for the mount.")
    name: str = Field(..., title="Name", description="The name of the mount.")
    s3_bucket_uri: str = Field(..., title="S3 Bucket URI", description="Which S3 URI to use for the mount.")

    @override
    def diff(self, other: BaseMountSpec) -> list[str]:
        d = super().diff(other)
        if isinstance(other, UploadS3BucketMountSpec):
            if other.name != self.name:
                d.append(f"name: {other.name} → {self.name}")
            if other.s3_bucket_uri != self.s3_bucket_uri:
                d.append(f"s3_bucket_uri: {other.s3_bucket_uri} → {self.s3_bucket_uri}")
        return d


class VolumeMountSpec(BaseMountSpec):
    mode: Literal["VOLUME"] = Field(..., title="Mode", description="The mode to use for the mount.")
    name: str = Field(..., title="Name", description="The name of the volume to mount.")

    @override
    def diff(self, other: BaseMountSpec) -> list[str]:
        d = super().diff(other)
        if isinstance(other, VolumeMountSpec) and self.name != other.name:
            d.append(f"name: {other.name} → {self.name}")
        return d


MountSpecUnion = Annotated[
    Union[DownloadMountSpec, DownloadS3BucketMountSpec, UploadMountSpec, UploadS3BucketMountSpec, VolumeMountSpec],
    Field(discriminator="mode"),
]


def diff_mount_spec(new: MountSpecUnion, existing: fragments.MountSpec) -> list[str]:
    """Returns a list of differences between a local and a remote mount spec."""
    return new.diff(remote_mount_spec_to_local(existing))


def remote_mount_spec_to_local(mount_spec: fragments.MountSpec) -> MountSpecUnion:
    if mount_spec.mode == "DOWNLOAD":
        tag = _filter_empty_remote_tags(mount_spec.tag)
        return DownloadMountSpec(
            mode="DOWNLOAD",
            path=mount_spec.path,
            selector=MountSelector(name=mount_spec.name, tag=tag, project=mount_spec.referenced_project_id),
        )
    elif mount_spec.mode == "DOWNLOAD_S3":
        return DownloadS3BucketMountSpec(
            mode="DOWNLOAD_S3", name=mount_spec.name, path=mount_spec.path, s3_bucket_uri=mount_spec.s3_bucket_uri or ""
        )
    elif mount_spec.mode == "UPLOAD":
        tag = _filter_empty_remote_tags(mount_spec.tag)
        return UploadMountSpec(mode="UPLOAD", path=mount_spec.path, target=MountTarget(name=mount_spec.name, tag=tag))
    elif mount_spec.mode == "UPLOAD_S3":
        return UploadS3BucketMountSpec(
            mode="UPLOAD_S3", name=mount_spec.name, path=mount_spec.path, s3_bucket_uri=mount_spec.s3_bucket_uri or ""
        )
    elif mount_spec.mode == "VOLUME":
        return VolumeMountSpec(mode="VOLUME", path=mount_spec.path, name=mount_spec.name)
    raise SlingshotException(f"Unknown mount mode: {mount_spec.mode}")


def _filter_empty_remote_tags(tags_str: str | None) -> str | None:
    """Parses comma separated tags string and returns None if there are no valid tags (empty tags are ignored)."""
    valid_tags = _filter_empty_tags(tags_str.split(',')) if tags_str else []
    return ",".join(valid_tags) if valid_tags else None


def _filter_empty_tags(tags: list[str]) -> list[str]:
    """Filters out empty tags."""
    return [tag.strip() for tag in tags if tag.strip()]
