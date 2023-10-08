import enum
from enum import Enum


class Database(Enum):
    ELASTICSEARCH = "elasticsearch"
    MONGO = "mongo"
    POSTGRES = "postgres"
    REDIS = "redis"


class Queue(Enum):
    RABBITMQ = "rabbitmq"
    REDPANDA = "redpanda"
