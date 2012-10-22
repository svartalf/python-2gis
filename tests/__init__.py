import os.path
import random
import multiprocessing
from wsgiref.simple_server import make_server
import unittest

import dgis


class BaseTestCase(unittest.TestCase):

    @staticmethod
    def response_handler(environ, start_response):
        start_response('200 OK', [('Content-Type', 'application/json'),])

        filename = '%s.json' % environ['PATH_INFO'].strip('/').replace('/', '_')
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'responses', filename)

        return open(file_path).read()

    def setUp(self):
        self.port = random.randint(10000, 65365)
        server = make_server('', self.port, self.response_handler)
        self.server_process = multiprocessing.Process(target=server.serve_forever)
        self.server_process.start()

        self.api = dgis.API('1234567890', host='127.0.0.1:%s' % self.port, register_views=False)
