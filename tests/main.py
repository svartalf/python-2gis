try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock
import dgis

from tests import MockGetRequest


class MainTest(unittest.TestCase):

    def setUp(self):
        self.blank_response = {
            'response_code': '200',
        }

    def test(self):
        api = dgis.API('1234567890')

        def validate(url):
            parts = urlparse.urlparse(url)
            query = urlparse.parse_qs(parts[4])

            self.assertEqual(api.version, query['version'][0])
            self.assertEqual(api.key, query['key'][0])
            self.assertEqual(parts[1], api.host)

        validator = MockGetRequest(validate, self.blank_response)

        with mock.patch('requests.get', validator):
            api.project_list()
