from source.infrastructure.layers.data_layer.abstract import AbstractDataLayer


class Elk(AbstractDataLayer):
    def __init__(self, resource_name: str) -> None:
        self.resource_name: str = resource_name
        super().__init__(resource_name=resource_name)

    def connection_alive(self) -> bool:
        pass

    def get_by_id(self, id: str) -> dict:
        pass

    def get_by_filter(self, filter, *args: any, **kwargs: any) -> list[dict]:
        pass

    def insert_item(self, item) -> str:
        pass

    def insert_list(self, itens: list[dict]) -> list[str]:
        pass

    def update_by_id(self, id: str, data: dict) -> tuple:
        pass

    def update_by_criteria(self, criteria: dict, data: dict) -> tuple:
        pass

    def delete_by_criteria(self, criteria: dict) -> tuple:
        pass
