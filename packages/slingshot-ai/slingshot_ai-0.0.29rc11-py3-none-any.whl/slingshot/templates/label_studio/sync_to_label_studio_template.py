"""
Label studio data script for syncing data from Slingshot to Label Studio

Configurable parameters:
- dataset_mount_path: Path to the dataset file.
  Default: /mnt/data/dataset.jsonl
- annotations_mount_path: Path to the annotations file.
  Default: /mnt/annotations/annotations.jsonl
- project_id: Which project ID to use on the label-studio side for syncing
  Default: 1
"""

import asyncio
import datetime
import json
import os
from pathlib import Path
from typing import Any

import label_studio_sdk
from pydantic import BaseModel

from slingshot import SlingshotSDK
from slingshot.schemas import Example, ExampleResult

DATASET_MOUNT_PATH = "/mnt/data/dataset.jsonl"
ANNOTATIONS_MOUNT_PATH = "/mnt/annotations/annotations.jsonl"

DATASET_ARTIFACT_NAME = "dataset"
DATASET_ARTIFACT_TAG = "latest"

# Add data field names here that contain paths to media files here.
# For example, if your data is shaped like {"example_id": "1", "img_path": "path/img.jpg"}, add "img_path".
MEDIA_PATH_FIELDS: list[str] = []


def read_slingshot_examples(path: Path) -> list[str]:
    """Read examples from a file as a list of raw JSON strings."""
    if not path.exists():
        return []

    examples = []
    with open(path, "r") as f:
        for line in f:
            if line := line.strip():
                examples.append(line)
    return examples


async def sync_tasks_to_label_studio(
    ls_client: label_studio_sdk.Client,
    sdk: SlingshotSDK,
    examples: list[Example],
    annotations: list[ExampleResult],
    project_id: int = 1,
) -> None:
    """SYnc examples to Label Studio as tasks."""
    latest_artifact = None
    if MEDIA_PATH_FIELDS:
        latest_artifact = await sdk.get_artifact(
            blob_artifact_name=DATASET_ARTIFACT_NAME, blob_artifact_tag=DATASET_ARTIFACT_TAG
        )
        # TODO: untangle the artifact obtained via SDK from the one mounted here.
        #  The SDK one is only used if there are media fields.
        assert sdk.project_id, "Slingshot SDK Project ID is not set"

    print(f"Syncing {len(examples)} examples as Label Studio annotation tasks")
    tasks = []
    for example in examples:
        data = example
        if isinstance(data, BaseModel):
            data = data.model_dump()
        if MEDIA_PATH_FIELDS:
            assert latest_artifact, f"No artifact found with name {DATASET_ARTIFACT_NAME} and tag 'latest'"
            data = await convert_media_paths_to_signed_urls(
                sdk=sdk, data=data, blob_artifact_id=latest_artifact.blob_artifact_id, project_id=sdk.project_id
            )
        tasks.append({"data": {**data, "example_id": example.example_id}})

    print("Syncing tasks to Label Studio")
    project = ls_client.get_project(id=project_id)
    task_ids: list[int] = project.import_tasks(tasks=tasks)

    print(f"Syncing {len(annotations)} existing annotations to Label Studio")
    example_ids_to_task_id = {example.example_id: task_id for example, task_id in zip(examples, task_ids)}
    for annotation in annotations:
        task_id = example_ids_to_task_id[annotation.example_id]
        project.create_annotation(task_id=task_id, result=annotation.result.model_dump())


async def convert_media_paths_to_signed_urls(
    sdk: SlingshotSDK, data: dict[str, Any], blob_artifact_id: str, project_id: str
) -> dict[str, Any]:
    """Convert media paths inside your dataset into signed URLs for Label Studio to load from."""
    for field in MEDIA_PATH_FIELDS:
        image_url_resp = await sdk.api.signed_url_blob_artifact(
            blob_artifact_id=blob_artifact_id,
            file_path=data[field],
            expiration=datetime.timedelta(days=7),
            project_id=project_id,
        )
        assert not image_url_resp.error, f"Error getting signed url: {image_url_resp.error}"
        assert image_url_resp.data, "No signed url returned"
        data[field] = image_url_resp.data.signed_url
    return data


async def main():
    """Sync the dataset from the mounted path to Label Studio as annotation tasks."""
    assert "LABEL_STUDIO_API_KEY" in os.environ, "Please create a Slingshot Secret for 'LABEL_STUDIO_API_KEY'"
    assert "LABEL_STUDIO_URL" in os.environ, "Please create a Slingshot Secret for 'LABEL_STUDIO_URL'"
    sdk = SlingshotSDK()
    await sdk.setup()

    config = json.loads(os.environ.get("CONFIG", "{}"))
    dataset_mount_path = Path(config.get("dataset_mount_path", DATASET_MOUNT_PATH))
    annotations_mount_path = Path(config.get("annotations_mount_path", ANNOTATIONS_MOUNT_PATH))
    project_id = int(config.get("project_id", 1))

    # Load all examples and annotations from the mounted paths
    example_json_strings = read_slingshot_examples(dataset_mount_path)
    annotation_json_strings = read_slingshot_examples(annotations_mount_path)

    examples = [Example.model_validate_json(example) for example in example_json_strings]
    annotations = [ExampleResult.model_validate_json(annotation) for annotation in annotation_json_strings]

    ls_client = label_studio_sdk.Client(api_key=os.environ["LABEL_STUDIO_API_KEY"], url=os.environ["LABEL_STUDIO_URL"])
    await sync_tasks_to_label_studio(
        ls_client, sdk=sdk, examples=examples, annotations=annotations, project_id=project_id
    )


if __name__ == "__main__":
    asyncio.run(main())
