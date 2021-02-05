"""
- How to test parse?
"""


class Parser(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_name(self, body):
        pass

    def extract_campaign(self, body):
        pass

    def parse(self):
        file_content = open(self.file_path, 'rb').read()

        return {
            'name': self.extract_name(file_content),
            'campaign': self.extract_campaign(file_content)
        }

# ----


class NameExtractor(object):
    pass


class CampaignExtractor(object):
    pass


class SrpParser(object):
    def __init__(self, file_path, extractors):
        pass
