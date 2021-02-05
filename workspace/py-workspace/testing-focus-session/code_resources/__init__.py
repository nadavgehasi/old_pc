import inspect
from datetime import datetime

from pytest import fixture


class TestClassBase(object):
    @classmethod
    def find_fixtures(cls, func, request):
        fixtures = {}
        arg_spec = inspect.getargspec(func)
        for index, arg in enumerate(arg_spec.args):
            if index == 0 and arg in ['self', 'cls']:
                continue
            fixtures[arg] = request.getfixturevalue(arg)

        return fixtures

    @fixture(autouse=True, scope='class')
    def init_class(self, request):
        setup_fixtures = self.find_fixtures(self.setup_test_class, request)
        teardown_fixtures = self.find_fixtures(self.teardown_test_class, request)

        self.__class__.setup_test_class(**setup_fixtures)
        yield
        self.__class__.teardown_test_class(**teardown_fixtures)

    @fixture(autouse=True)
    def init(self, request):
        setup_fixtures = self.find_fixtures(self.setup_test, request)
        teardown_fixtures = self.find_fixtures(self.teardown_test, request)

        self.setup_test(**setup_fixtures)
        yield
        self.teardown_test(**teardown_fixtures)

    def setup_test(self, **fixtures):
        pass

    def teardown_test(self, **fixtures):
        pass

    @classmethod
    def setup_test_class(cls, **fixtures):
        pass

    @classmethod
    def teardown_test_class(cls, **fixtures):
        pass


def extract_year(value):
    if isinstance(value, int):
        return value
    if isinstance(value, datetime):
        return value.year
    raise NotImplementedError


class Worker(object):
    def __init__(self, task, name=None):
        self.task = task
        self.name = name

    def work_hard(self):
        self.task.run()

    def rest(self):
        pass

    def set_rest_time(self, rest_time):
        pass

    def fire(self):
        pass


class FastWorker(Worker):
    pass


class Connection(object):
    def __init__(self, port):
        self.port = port

    def connect(self):
        pass

    def disconnect(self):
        pass
