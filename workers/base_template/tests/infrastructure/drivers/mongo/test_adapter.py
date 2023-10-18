from source.infrastructure.drivers.mongo.adapter import Mongo


def test_mongo_connection_alive():
    mongo = Mongo("default")
    assert mongo.connection_alive() == True
