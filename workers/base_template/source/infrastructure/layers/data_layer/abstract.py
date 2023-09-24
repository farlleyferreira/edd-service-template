from abc import ABC, abstractmethod
from project.helpers.pydantic_typo import ObjectId


class AbstractDataLayer(ABC):  # pragma: no cover
    def __init__(self, resource_name: str):
        self.resource_name: str = resource_name
        super().__init__()

    @abstractmethod
    async def get_buildinfo(self) -> bool:
        pass

    @abstractmethod
    async def get_by_id(self, id: str) -> dict:
        pass

    @abstractmethod
    async def get_by_filter(self, filter, *args: any, **kwargs: any) -> list[dict]:
        pass

    @abstractmethod
    async def insert_item(self, item) -> ObjectId:
        pass

    @abstractmethod
    async def insert_list(self, itens: list[dict]) -> list[ObjectId]:
        pass

    @abstractmethod
    async def update_by_id(self, id: ObjectId, data: dict) -> tuple:
        pass

    @abstractmethod
    async def update_by_criteria(self, criteria: dict, data: dict) -> tuple:
        pass

    @abstractmethod
    async def delete_by_criteria(self, criteria: dict) -> tuple:
        pass
