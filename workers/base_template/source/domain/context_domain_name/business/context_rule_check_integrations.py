import concurrent.futures
from source.helpers.constants.technologies import Database, Queue
from source.infrastructure.layers.data_layer.concrete import DataLayer
from source.infrastructure.layers.queue_layer.concrete import QueueLayer


class CheckIntegrations(object):
    def __init__(self):
        ...

    def check_database_status(self, technology, resource_name):
        data_layer = DataLayer(technology, resource_name)
        print(technology)
        return data_layer.connection_alive()

    def check_queue_status(self, technology, resource_name):
        queue_layer = QueueLayer(technology, resource_name)
        print(technology)
        return queue_layer.connection_alive()

    def execute_multithread(self, process, params, max_threads, process_name) -> any:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            results = list(executor.map(process, params, [process_name] * max_threads))
            print(process_name)
            return results

    def check_databases(self) -> bool:
        try:
            databases = [
                Database.ELASTICSEARCH,
                Database.POSTGRES,
                Database.REDIS,
                Database.MONGO,
            ]

            results = self.execute_multithread(
                process=self.check_database_status,
                params=databases,
                max_threads=len(databases),
                process_name="checkbuildinfo",
            )

            return all(results)
        except Exception as error:
            raise error

    def check_queue(self) -> bool:
        try:
            queues = [
                Queue.RABBITMQ,
                Queue.REDPANDA,
            ]

            results = self.execute_multithread(
                process=self.check_queue_status,
                params=queues,
                max_threads=len(queues),
                process_name="checkbrokerinfo",
            )
            return all(results)
        except Exception as error:
            raise error

    def integrations_status(self, process_id) -> bool:
        try:
            check_integration_status = [
                self.check_queue(),
                self.check_databases(),
            ]

            print(f"PID: {process_id}")
            return all(check_integration_status)

        except Exception as error:
            raise error
