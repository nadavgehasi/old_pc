"""
- every add of extractor will broke tests of parser
"""


class Parser(object):
    def __init__(self, file_path, name_extractor, campaign_extractor):
        self.file_path = file_path
        self.name_extractor = name_extractor
        self.campaign_extractor = campaign_extractor

    def parse(self):
        file_content = open(self.file_path, 'rb').read()

        return {
            'name': self.name_extractor.extract(file_content),
            'campaign': self.campaign_extractor.extract(file_content)
        }
