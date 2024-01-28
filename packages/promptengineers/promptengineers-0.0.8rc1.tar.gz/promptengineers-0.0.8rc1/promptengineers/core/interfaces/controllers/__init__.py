from abc import ABC, abstractmethod
from typing import Any, Dict

class IController(ABC):
    @abstractmethod
    async def index(self, page: int, limit: int) -> Any:
        pass

    @abstractmethod
    async def create(self, body: Dict) -> Any:
        pass

    @abstractmethod
    async def show(self, id: str) -> Any:
        pass

    @abstractmethod
    async def update(self, id: str, body: Dict) -> Any:
        pass

    @abstractmethod
    async def delete(self, id: str) -> Any:
        pass
