# -*- coding: utf-8 -*-

try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
import unittest

import six
import mock
import dgis

from tests import MockGetRequest, load_response


class RubricatorTest(unittest.TestCase):

    def setUp(self):
        # From the `http://api.2gis.ru/doc/firms/list/rubricator/'_
        self.response = load_response('rubricator.json')

    def test(self):
        api = dgis.API('1234567890')

        def validate(url):
            parts = urlparse.urlparse(url)
            query = urlparse.parse_qs(parts[4])

            self.assertIn('where', query)

            # Boolean value should be converted into a integer
            self.assertIn('show_children', query)
            self.assertEqual('1', query['show_children'][0])

        validator = MockGetRequest(validate, self.response)

        with mock.patch('requests.get', validator):
            api.rubricator(where=six.u('Иркутск'), show_children=True)
