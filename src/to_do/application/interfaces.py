from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

T = TypeVar("T")
V = TypeVar("V")


class Repository(ABC, Generic[T, V]):
    @abstractmethod
    def add(self, obj: T) -> None:
        pass

    @abstractmethod
    def get(self, obj_id: V) -> T:
        pass

    @abstractmethod
    def remove(self, obj_id: V) -> None:
        pass

    @abstractmethod
    def update(self, obj: T) -> None:
        pass
