import os
from pymongo import MongoClient


class MongoConnector:
    def __init__(self) -> None:
        self.port = os.getenv("MONGO_PORT")
        self.host: str = os.getenv("MONGO_HOST")
        self.username: str = os.getenv("MONGO_USERNAME")
        self.password: str = os.getenv("MONGO_PASSWORD")

    def create_client(self) -> MongoClient:
        if not self.host:
            raise ValueError("host is not defined.")

        try:
            uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"
            client = MongoClient(uri)
            return client
        except Exception as error:
            raise error
