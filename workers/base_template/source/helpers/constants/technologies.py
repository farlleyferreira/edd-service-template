import enum
from enum import Enum


class Database(Enum):
    ELASTICSEARCH = "elasticsearch"
    MONGO = "mongo"
    POSTGRES = "postgres"
    REDIS = "redis"
