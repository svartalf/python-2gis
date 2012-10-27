# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
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

from tests import MockGetRequest, load_response, skip_if_no_api_key


class RubricatorTest(unittest.TestCase):

    def setUp(self):
        # From the `http://api.2gis.ru/doc/firms/list/rubricator/'_
        self.response = load_response('rubricator.json')

    @unittest.skipIf(False, '')
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
            api.rubricator(where='Иркутск', show_children=True)


    @skip_if_no_api_key
    def test_real(self):
        api = dgis.API(os.environ['DGIS_KEY'])
        response = api.rubricator(where='Иркутск', show_children=True)

        self.assertEqual(int(response['total']), len(response['result']))
