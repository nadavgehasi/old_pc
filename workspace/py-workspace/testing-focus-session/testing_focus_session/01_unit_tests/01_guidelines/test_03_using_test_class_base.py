"""
Using TestClassBase
"""

from mock import Mock
from pytest import raises

from code_resources import TestClassBase, Worker


class TestWorker(TestClassBase):
    def setup_test(self, monkeypatch):
        self.mocked_task = Mock(spec_set=['run'])

        self.tested = Worker(self.mocked_task)

    def test_work_hard__task_finish_correctly__did_hard_work(self):
        ###
        self.tested.work_hard()
        ###

    def test_work_hard__task_raise_exception__exception_raised(self):
        self.mocked_task.run.side_effect = Exception()

        ###
        with raises(Exception):
            self.tested.work_hard()
        ###
