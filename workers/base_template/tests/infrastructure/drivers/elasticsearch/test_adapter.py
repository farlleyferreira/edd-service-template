from source.infrastructure.drivers.elasticsearch.adapter import Elasticsearch


def test_elasticsearch_connection_alive():
    elasticsearch = Elasticsearch("default")
    assert elasticsearch.connection_alive() == True
