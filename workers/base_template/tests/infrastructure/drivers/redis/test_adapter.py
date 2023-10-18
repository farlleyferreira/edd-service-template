from source.infrastructure.drivers.redis.adapter import Redis


def test_redis_connection_alive():
    redis = Redis("default")
    assert redis.connection_alive() == True
