# -*- coding: utf-8 -*-

try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
import unittest

import mock
import dgis

from tests import MockGetRequest, load_response


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
