"""
Too Short Assertion
"""
from mock import Mock

from code_resources import TestClassBase, Worker


class TestSomeClass(TestClassBase):
    def setup_test(self):
        self.mocked_task = Mock()

        self.tester = Worker(self.mocked_task)

    def assert_all(self):
        pass

    def test_consume__pasten__pasten(self):
        ###
        self.tester.work_hard()
        ###

        self.assert_all()
