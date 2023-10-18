import os
from elasticsearch import Elasticsearch


class ElasticsearchConnector(object):
    def __init__(self) -> None:
        self.hosts = os.getenv("ELASTIC_HOSTS")
        self.username = os.getenv("ELASTIC_USERNAME")
        self.password = os.getenv("ELASTIC_PASSWORD")

    def create_client(self) -> Elasticsearch:
        if not self.hosts:
            raise ValueError("host is not defined.")

        try:
            nodes = self.hosts.split(",")
            username = self.username
            password = self.password

            client = Elasticsearch(nodes, basic_auth=(username, password))

            return client

        except Exception as error:
            raise error
