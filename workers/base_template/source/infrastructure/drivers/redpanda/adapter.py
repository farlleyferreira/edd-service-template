from source.infrastructure.layers.queue_layer.abstract import AbstractQueueLayer


class RedPanda(AbstractQueueLayer):  # pragma: no cover
    def __init__(self, resource_name: str):
        self.resource_name: str = resource_name
        super().__init__(resource_name=resource_name)

    def connection_alive(self) -> bool:
        pass

    def send_data(self, data: object) -> object:
        pass

    def get_data(self, data: object) -> object:
        pass
