import pytest


class TestNothing(object):
    @pytest.fixture(autouse=True)
    def before_and_after(self):
        print('before')
        print(self)
        yield
        print('after')

    @classmethod
    @pytest.fixture(autouse=True, scope='class')
    def before_and_after_class(cls):
        print('before_class')
        yield
        print('after_class')

    def test_nothing_1(self):
        print('nothing_1')

    def test_nothing_2(self):
        print('nothing_2')
