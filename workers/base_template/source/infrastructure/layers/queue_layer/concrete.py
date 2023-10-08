# pragma: no cover
from source.helpers.constants.technologies import Queue
from source.infrastructure.drivers.redpanda.adapter import RedPanda
from source.infrastructure.drivers.rabbitmq.adapter import RabbitMq


class QueueLayer:  # pragma: no cover
    def __init__(
        self, technology: Queue = Queue.RABBITMQ, resource_name: str = "default"
    ) -> None:
        technology_mapping = {
            Queue.REDPANDA: RedPanda,
            Queue.RABBITMQ: RabbitMq,
        }

        self.instance = technology_mapping.get(technology, Queue.RABBITMQ)(
            resource_name
        )

    def __getattr__(self, name):
        return self.instance.__getattribute__(name)
