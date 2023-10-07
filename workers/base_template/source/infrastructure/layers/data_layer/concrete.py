# pragma: no cover
from source.helpers.constants.technologies import Database
from source.infrastructure.drivers.elasticsearch.adapter import Elk
from source.infrastructure.drivers.postgre.adapter import Postgre
from source.infrastructure.drivers.redis.adapter import Redis
from source.infrastructure.drivers.mongo.adapter import Mongo


class DataLayer:  # pragma: no cover
    def __init__(
        self, technology: Database = Database.MONGO, resource_name: str = "default"
    ) -> None:
        technology_mapping = {
            Database.ELASTICSEARCH: Elk,
            Database.POSTGRES: Postgre,
            Database.REDIS: Redis,
            Database.MONGO: Mongo,
        }

        self.instance = technology_mapping.get(technology, Database.MONGO)(
            resource_name
        )

    def __getattr__(self, name):
        return self.instance.__getattribute__(name)
