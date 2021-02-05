"""
Fixtures Mess
* fixture can have hidden logic
* arrangement is less understandable
"""
from code_resources import TestClassBase


class TestSomeClass(TestClassBase):
    def test_consume__pasten__pasten(self, file_consumer, file_producer, ids_to_produce,
                                     patch_env, prepare_db):
        for id_to_produce in ids_to_produce:
            produced = file_producer.produce(id_to_produce)
            assert file_consumer.consume(produced) is True
