from abc import abstractmethod
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class HasAutoscalingParams(Protocol):
    @property
    @abstractmethod
    def min_replicas(self) -> int | None:
        ...

    @property
    @abstractmethod
    def max_replicas(self) -> int | None:
        ...


@runtime_checkable
class HasComponentConfig(Protocol):
    @property
    @abstractmethod
    def config_variables(self) -> dict[str, Any]:
        ...


@runtime_checkable
class HasProjectCredentials(Protocol):
    @property
    @abstractmethod
    def attach_project_credentials(self) -> bool:
        ...
