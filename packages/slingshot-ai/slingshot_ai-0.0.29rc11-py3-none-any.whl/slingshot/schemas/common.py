from pydantic import BaseModel, ConfigDict


class SlingshotBaseModel(BaseModel):
    model_config = ConfigDict(extra='forbid')


ALPHANUMERIC_UNDERSCORE_HYPHEN_RE = "^[A-Za-z][A-Za-z0-9_-]*$"  # This should match the regex on the backend

REPO = "https://github.com/slingshot-ai/slingshot"
PATH_TO_FILE = "slingshot_client/src/slingshot/schemas"
FILENAME = "slingshot-schema.config.json"
FILE_LOCATION = "/".join([REPO, "blob/main", PATH_TO_FILE, FILENAME])
