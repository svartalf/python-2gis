import os.path
import json


class MockResponse(object):
    """Mock replacement for a response object
    returned by a `requests.get` function"""

    def __init__(self, json):
        self._json = json

    @property
    def json(self):
        return self._json

    @property
    def text(self):
        """This property is used only with a `register_views` parameter,
        so we can freely return a '1' text, which means, that view had been registered"""

        return '1'

class MockGetRequest(object):
    """Mock replacement for a `requests.get` function"""

    def __init__(self, validator, json):
        self.validator = validator
        self.json = json

    def __call__(self, url):
        self.validator(url)

        return MockResponse(self.json)


def load_response(filename):
    try:
        f = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'responses', filename))
        return json.load(f)
    finally:
        f.close()
