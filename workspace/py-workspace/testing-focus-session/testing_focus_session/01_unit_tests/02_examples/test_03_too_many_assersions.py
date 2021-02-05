"""
Too Many Assertion
"""
from mock import Mock

from code_resources import TestClassBase, Worker


class TestSomeClass(TestClassBase):
    def setup_test(self):
        self.mocked_task = Mock()

        self.tester = Worker(self.mocked_task)

    def test_consume__pasten__pasten(self):
        ###
        self.tester.work_hard()
        ###

        for plan in self.tester.task.plans:
            for mission in plan.missions:
                assert mission.plan == plan
        assert self.tester.task.length == 20
        assert self.mocked_task.call_count == 2
        assert self.mocked_task.mock_calls[0][1][0] == ('a', '2')
