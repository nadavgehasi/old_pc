from pytest import fixture

from code_resources import Connection


@fixture
def connections(request):
    ports = getattr(request.module, "ports", [])
    connections = []
    for port in ports:
        connection = Connection(port)
        connection.connect()
        connections.append(connection)
        request.addfinalizer(connection.disconnect)
    return connections
