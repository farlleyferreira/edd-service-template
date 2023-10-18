import redis
import os


class RedisConnector(object):
    def __init__(self):
        self.host: str = os.getenv("REDIS_HOST")
        self.port = int(os.getenv("REDIS_PORT"))
        self.password: str = os.getenv("REDIS_PASSWORD")

    def create_client(self):
        if not self.host:
            raise ValueError("host is not defined.")

        try:
            client = redis.Redis(host=self.host, port=self.port, password=self.password)
            return client
        except Exception as error:
            raise error
