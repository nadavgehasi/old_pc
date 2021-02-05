from code_resources import TestClassBase, Worker


class TestNothing(TestClassBase):
    @classmethod
    def get_test_data(cls):
        return 'task1'

    def setup_test(self):
        test_data = self.get_test_data()
        self.tester = Worker(test_data)


class TestOtherNothing(TestNothing):
    @classmethod
    def get_test_data(cls):
        return 'task2'
