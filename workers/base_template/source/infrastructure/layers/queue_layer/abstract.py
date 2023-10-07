from abc import ABC, abstractmethod


class AbstractQueueLayer(ABC):  # pragma: no cover
    def __init__(self, resource_name: str):
        self.resource_name: str = resource_name
        super().__init__()

    @abstractmethod
    async def connection_alive(self) -> bool:
        pass

    @abstractmethod
    async def send_data(self, data: object) -> object:
        pass

    @abstractmethod
    async def get_data(self, data: object) -> object:
        pass
