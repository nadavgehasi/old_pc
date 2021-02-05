ports = [80, 433, 8080, 8000]


def test_connections(connections):
    for c in connections:
        print(c.port)
