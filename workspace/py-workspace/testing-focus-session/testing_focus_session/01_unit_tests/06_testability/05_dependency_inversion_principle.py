"""
- How to isolate the test?
"""


class NameExtractor(object):
    def extract(self, file_content):
        pass


class CampaignExtractor(object):
    def extract(self, file_content):
        pass


class Parser(object):
    def __init__(self, file_path, name_extractor=None):
        self.file_path = file_path
        self.name_extractor = name_extractor or NameExtractor()
        self.campaign_extractor = CampaignExtractor()

    def extract_name(self, body):
        pass

    def extract_campaign(self, body):
        pass

    def parse(self):
        file_content = open(self.file_path, 'rb').read()

        return {
            'name': self.name_extractor.extract(file_content),
            'campaign': self.campaign_extractor.extract(file_content)
        }
