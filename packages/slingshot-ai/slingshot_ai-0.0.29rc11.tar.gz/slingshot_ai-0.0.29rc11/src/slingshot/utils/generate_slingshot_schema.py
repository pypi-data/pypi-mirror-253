from __future__ import annotations

import json
import typing
from pathlib import Path

from slingshot.schemas import ProjectManifest
from slingshot.schemas.common import FILENAME, PATH_TO_FILE

if typing.TYPE_CHECKING:
    pass


if __name__ == "__main__":
    with open(Path(PATH_TO_FILE) / FILENAME, "w") as f:
        json.dump(ProjectManifest.model_json_schema(), f, indent=2)
