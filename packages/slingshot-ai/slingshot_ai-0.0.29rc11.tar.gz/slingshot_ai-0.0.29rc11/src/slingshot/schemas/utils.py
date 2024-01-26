import re
import typing

from slingshot.sdk import backend_schemas


class RequirementsParsingError(ValueError):
    pass


def requested_requirements_from_str(line: str) -> backend_schemas.RequestedRequirement:
    """Parses and creates a requested requirements instance from a string."""
    # NOTE: This is a standalone helper function rather than a static method as we do not import schema_extensions
    # during typing.
    if not line:
        raise RequirementsParsingError("empty requirement")
    if line.startswith("--"):  # --index-url or --extra-index-url
        raise RequirementsParsingError(f"Unsupported requirement {line}")

    if line.startswith("-"):  # -r or -e or -c
        raise RequirementsParsingError(f"Unsupported requirement {line}")

    match = re.match(r"([^\s>=@<~]+) *(==|@|>=|<=|~=|>|<)? *(\S+)?", line)
    if match is None:
        raise RequirementsParsingError(f"Unsupported requirement {line}")
    library, pin, version = match.groups()
    try:
        # Regex ensures that pin matches literal but mypy doesn't know that - force it
        return backend_schemas.RequestedRequirement(library=library.strip(), version=version and version.strip(), pin=pin and pin.strip())  # type: ignore
    except ValueError as e:
        raise RequirementsParsingError(f"Unsupported requirement {line}") from e


def has_path_ending_in_filename(path: str) -> bool:
    """
    Checks if the given path string ends with a pattern that looks like a file extension,
    i.e., a sequence of characters that are neither dots nor slashes, followed by a dot,
    and then followed by characters that are neither dots nor slashes until the end of the string.

    Args:
        path (str): The path string to be checked.

    Returns:
        bool: True if the pattern is found, False otherwise.

    Examples:
        >>> has_path_ending_in_filename('file.txt')
        True
        >>> has_path_ending_in_filename('/path/to/file.jpg')
        True
        >>> has_path_ending_in_filename('/path.with.dots/to/file')
        False
        >>> has_path_ending_in_filename('/path.with.dots/...file')
        False
        >>> has_path_ending_in_filename('/path.with.dots/file...')
        False
    """
    return re.search(r'[^./]+\.[^./]+$', path) is not None


def strip_keys_with_none_values(dict: dict[str, typing.Any]) -> dict[str, typing.Any]:
    """
    Strips all keys with None values from the given dictionary. We require this as the remote
    sometimes contain "flat" types, e.g. for the MountSpec type with all properties as optinal,
    whereas the client schema uses specific subclasses, each of which has its own schema for
    validation. By stripping out keys set to None, we avoid triggering complaints about extra
    keys which otherwise would fail the validation.

    Args:
        dict (dict[str, Any]): The dictionary to be stripped.

    Returns:
        dict[str, Any]: The stripped dictionary.

    Examples:
        >>> strip_keys_with_none_values({'a': 1, 'b': None, 'c': 2})
        {'a': 1, 'c': 2}
    """
    return {k: v for k, v in dict.items() if v is not None}


_machine_size_to_machine_type_gpu_count: dict[backend_schemas.MachineSize, tuple[backend_schemas.MachineType, int]] = {
    backend_schemas.MachineSize.CPU_1X: (backend_schemas.MachineType.CPU_TINY, 0),
    backend_schemas.MachineSize.CPU_2X: (backend_schemas.MachineType.CPU_SMALL, 0),
    backend_schemas.MachineSize.CPU_4X: (backend_schemas.MachineType.CPU_MEDIUM, 0),
    backend_schemas.MachineSize.CPU_8X: (backend_schemas.MachineType.CPU_LARGE, 0),
    backend_schemas.MachineSize.T4: (backend_schemas.MachineType.T4, 1),
    backend_schemas.MachineSize.L4: (backend_schemas.MachineType.L4, 1),
    backend_schemas.MachineSize.A100: (backend_schemas.MachineType.A100, 1),
    backend_schemas.MachineSize.A100_8X: (backend_schemas.MachineType.A100, 8),
}

_machine_type_gpu_count_to_machine_size: dict[tuple[backend_schemas.MachineType, int], backend_schemas.MachineSize] = {
    v: k for k, v in _machine_size_to_machine_type_gpu_count.items()
}


def machine_size_to_machine_type_gpu_count(
    machine_size: backend_schemas.MachineSize,
) -> tuple[backend_schemas.MachineType, int]:
    if machine_size not in _machine_size_to_machine_type_gpu_count:
        raise ValueError(f"Unknown machine size {machine_size}")
    return _machine_size_to_machine_type_gpu_count[machine_size]


def machine_type_gpu_count_to_machine_size(
    machine_type: backend_schemas.MachineType, gpu_count: int | None
) -> backend_schemas.MachineSize:
    if gpu_count is None:
        gpu_count = 0
    if (machine_type, gpu_count) not in _machine_type_gpu_count_to_machine_size:
        raise ValueError(f"Unknown machine type {machine_type} with {gpu_count} GPUs")
    return _machine_type_gpu_count_to_machine_size[(machine_type, gpu_count)]


def get_default_num_gpu(machine_type: backend_schemas.MachineType) -> int:
    cpu_machine_types = {
        backend_schemas.MachineType.CPU_TINY,
        backend_schemas.MachineType.CPU_SMALL,
        backend_schemas.MachineType.CPU_MEDIUM,
        backend_schemas.MachineType.CPU_LARGE,
    }
    # CPU machines have no GPUs
    if machine_type in cpu_machine_types:
        return 0
    return 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
