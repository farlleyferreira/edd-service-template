import os
import sqlalchemy as SqlDatabase
from sqlalchemy import Engine


class ElasticsearchConnector(object):
    def __init__(self) -> None:
        self.host = os.getenv("ELK_HOSTS")
        self.username = os.getenv("ELK_USERNAME")
        self.password = os.getenv("ELK_PASSWORD")
        self.database = os.getenv("ELK_PASSWORD")
        self.protocol = os.getenv("ELK_PASSWORD")

    def create_client(self) -> Engine:
        if not self.host:
            raise ValueError("host is not defined.")

        try:
            uri = f"{self.protocol}://{self.username}:{self.password}@{self.host}/{self.database}"
            client = SqlDatabase.create_engine(uri)
            return client

        except Exception as error:
            raise error
