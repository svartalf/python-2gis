# -*- coding: utf-8 -*-

try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
import unittest

import mock
import dgis

from tests import MockGetRequest


class ProjectListTest(unittest.TestCase):

    def setUp(self):
        # From the `http://api.2gis.ru/doc/firms/list/project-list/'_
        self.response = {
            'api_version': "1.3",
            'response_code': "200",
            'total': 69,
            'result': [
                {
                    'id': 1,
                    'name': u"Новосибирск",
                    'code': "novosibirsk",
                    'language': "ru",
                    'timezone': "Asia/Novosibirsk",
                    'min_zoomlevel': 9,
                    'max_zoomlevel': 17,
                    'centroid': "POINT(83.062249469999145 54.956108471916146)",
                    'transport': True,
                    'traffic': True,
                    'flamp': True,
                    'zoomlevel': 11,
                    'firmscount': 42839,
                    'filialscount': 60975,
                    'rubricscount': 953,
                    'geoscount': 143452,
                    'country_code': "ru"
                }
            ]
        }

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
