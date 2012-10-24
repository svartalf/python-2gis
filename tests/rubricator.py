# -*- coding: utf-8 -*-

try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
import unittest

import mock
import dgis

from tests import MockGetRequest


class RubricatorTest(unittest.TestCase):

    def setUp(self):
        # From the `http://api.2gis.ru/doc/firms/list/rubricator/'_
        self.response = {
            'api_version': "1.3",
            'response_code': "200",
            'parent_id': "140857747439618",
            'total': "38",
            'result': [
                {
                    'id': "140857747440153",
                    'name': u"Аквапарки / Водные аттракционы",
                    'alias': "akvaparki_vodnye_attrakciony",
                    'parent_id': "140857747439618"
                },
                {
                    'id': "140857747440562",
                    'name': u"Бани / Сауны",
                    'alias': "bani_sauny",
                    'parent_id': "140857747439618"
                }
            ]
        }

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
            api.rubricator(where=u'Иркутск', show_children=True)
