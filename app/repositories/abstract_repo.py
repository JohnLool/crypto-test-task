from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar("T")


class AbstractRepository(ABC, Generic[T]):
    @abstractmethod
    async def add(self, obj: T) -> T:
        pass

    @abstractmethod
    async def get_list(self, *, offset: int = 0, limit: int = 100) -> List[T]:
        pass
