"""
- Tests Reuse
- parse test getting complicated
"""


class Extractor(object):
    def extract(self, file_content):
        pass


class NameExtractor(object):
    def initialize(self):
        pass

    def extract(self, file_content):
        return file_content


class Parser(object):
    def __init__(self, file_content, extractors):
        self.file_content = file_content
        self.extractors = extractors

    def parse(self):
        parsed = {}
        for extractor in self.extractors:
            if isinstance(extractor, NameExtractor):
                extractor.initialize()
            parsed[extractor.name] = extractor.extract(self.file_content)
        return parsed
