from source.helpers.constants.technologies import Database


class DataLayer:
    def __init__(
        self, technology: Database = Database.MONGO, resource_name: str = "healthcheck"
    ) -> None:
        technology_mapping = {
            Database.ELASTICSEARCH: object,
            Database.POSTGRES: object,
            Database.REDIS: object,
            Database.MONGO: object,
        }

        self.instance = technology_mapping.get(technology, Database.MONGO)(
            resource_name
        )

    def __getattr__(self, name):
        return self.instance.__getattribute__(name)
