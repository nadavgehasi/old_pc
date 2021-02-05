from pytest import fixture


@fixture
def one(): return 1


@fixture
def three(): return 3


@fixture
def one_and_two(one): return [one, 2]


def test_something(one_and_two, three):
    assert one_and_two + [three] == [1, 2, 3]
