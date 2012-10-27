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


class ProjectListTest(unittest.TestCase):

    def setUp(self):
        # From the `http://api.2gis.ru/doc/firms/list/project-list/'_
        self.response = load_response('project_list.json')

    def test(self):
        api = dgis.API('1234567890')

        def validate(url):
            parts = urlparse.urlparse(url)
            query = urlparse.parse_qs(parts[4])

            # Assert that there is no more any parameters
            self.assertEqual(len(query), 3)

        validator = MockGetRequest(validate, self.response)

        with mock.patch('requests.get', validator):
            api.project_list()

    @skip_if_no_api_key
    def test_real(self):
        api = dgis.API(os.environ['DGIS_KEY'])
        response = api.project_list()

        self.assertGreater(response['total'], 0)
        self.assertEqual(response['total'], len(response['result']))
