import os
import sqlalchemy as SqlDatabase
from sqlalchemy import Engine


class PostgreConnector(object):
    def __init__(self) -> None:
        self.host = os.getenv("POSTGRE_HOST")
        self.username = os.getenv("POSTGRE_USERNAME")
        self.password = os.getenv("POSTGRE_PASSWORD")
        self.database = os.getenv("POSTGRE_DATABASE")
        self.protocol = os.getenv("POSTGRE_PROTOCOL")

    def create_client(self) -> Engine:
        if not self.host:
            raise ValueError("host is not defined.")

        try:
            uri = f"{self.protocol}://{self.username}:{self.password}@{self.host}"
            client = SqlDatabase.create_engine(uri)
            return client

        except Exception as error:
            raise error
