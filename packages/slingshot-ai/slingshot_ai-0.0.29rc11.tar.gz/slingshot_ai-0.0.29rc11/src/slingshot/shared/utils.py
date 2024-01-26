from __future__ import annotations

import json
import os
import typing
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from pydantic import BaseModel
from ruamel import yaml as r_yaml

from slingshot.sdk import backend_schemas
from slingshot.sdk.errors import SlingshotException

yaml = r_yaml.YAML()

T = typing.TypeVar("T")


class ResponseProtocol(typing.Protocol[T]):
    data: typing.Optional[T]
    error: typing.Optional[backend_schemas.SlingshotLogicalError]


def get_data_or_raise(resp: ResponseProtocol[T]) -> T:
    if resp.error:
        raise SlingshotException(resp.error.message)
    if resp.data is None:
        raise SlingshotException("No data returned from server")
    return resp.data


def pydantic_to_dict(pydantic: BaseModel, *, exclude_unset: bool = True) -> dict[str, Any]:
    # Convert enums to strings
    return json.loads(pydantic.model_dump_json(exclude_none=True, exclude_unset=exclude_unset))


@contextmanager
def enter_path(path: Path | str) -> typing.Generator[None, None, None]:
    """
    Changes the working directory to the specified, restoring it back to the original one when the context manager closes.
    """
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)
