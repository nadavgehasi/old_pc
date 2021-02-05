import mock
from pytest import fixture

from code_resources import Worker


@fixture
def make_worker():
    created_records = []

    def _make_worker(name):
        _record = Worker(mock.Mock(), name=name)
        created_records.append(_record)
        return _record

    yield _make_worker

    for record in created_records:
        record.fire()


def test_customer_records(make_worker):
    make_worker("Noa")
    make_worker("Omri")
    make_worker("Assaf")
