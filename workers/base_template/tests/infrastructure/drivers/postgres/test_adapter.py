from source.infrastructure.drivers.postgre.adapter import Postgre


def test_postgre_connection_alive():
    postgre = Postgre("default")
    assert postgre.connection_alive() == True
