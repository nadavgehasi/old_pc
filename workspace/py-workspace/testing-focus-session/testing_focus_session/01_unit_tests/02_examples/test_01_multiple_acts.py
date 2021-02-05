"""
Multiple acts in one test function
* tests are not isolated
* when test failed you can't see which one
"""

from mock import Mock

from code_resources import TestClassBase, Worker


class TestSomeClass(TestClassBase):
    def setup_test(self):
        self.mocked_task = Mock()

        self.tester = Worker(self.mocked_task)

    def test_work_hard(self):
        self.tester.set_rest_time(20)

        ###
        self.tester.rest()
        ###

        self.tester.set_rest_time(None)

        ###
        self.tester.rest()
        ###

        self.tester.set_rest_time('42')

        ###
        self.tester.rest()
        ###
