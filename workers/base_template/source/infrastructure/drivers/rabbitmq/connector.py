import os
from typing import Coroutine
import aio_pika


class RabbitMqConnector:
    def __init__(self) -> None:
        self.port = os.getenv("RABBITMQ_HOST")
        self.host: int = int(os.getenv("RABBITMQ_PORT"))
        self.username: str = os.getenv("RABBITMQ_USERNAME")
        self.password: str = os.getenv("RABBITMQ_PASSWORD")

    def create_client(self) -> Coroutine:
        if not self.host:
            raise ValueError("host is not defined.")

        try:
            client = aio_pika.connect(
                host=self.host,
                port=self.port,
                login=self.username,
                password=self.password,
            )

            return client
        except Exception as error:
            raise error
