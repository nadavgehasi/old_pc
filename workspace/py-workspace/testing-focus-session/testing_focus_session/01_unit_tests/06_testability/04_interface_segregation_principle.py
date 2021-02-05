"""
- Tests of subclasses can be broken if the interfaces will be changes
"""


class Extractor(object):
    def extract(self):
        raise NotImplementedError()

    def serialize(self):
        raise NotImplementedError()

    def validate_encoding(self):
        raise NotImplementedError()

    def convert_to_number(self):
        raise NotImplementedError()
