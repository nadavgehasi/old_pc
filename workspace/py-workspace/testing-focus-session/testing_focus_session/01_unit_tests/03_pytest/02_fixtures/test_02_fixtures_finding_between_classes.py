from pytest import fixture

from code_resources import Worker, FastWorker


class TestWorker(object):
    @fixture
    def tested(self):
        return Worker('task')

    def test_something(self, tested):
        assert isinstance(tested, Worker)

class TestFastWorker(object):
    @fixture
    def tested(self):
        return FastWorker('task')

    def test_something(self, tested):
        assert isinstance(tested, FastWorker)
