# -*- coding: utf-8 -*-

import json
import os.path
import hashlib
import urlparse
import urllib

import requests

from dgis.exceptions import DgisError
from dgis.utils import smart_str

__all__ = ('bind_api',)


def __init__(self, api):
    self.api = api


def execute(self, *args, **kwargs):

    # Build GET parameters for query
    parameters = {}

    # Both positional
    for idx, arg in enumerate(args):
        if arg is None:
            continue

        try:
            parameters[self.allowed_param[idx]] = smart_str(arg)
        except IndexError:
            raise ValueError('Too many parameters supplied')

    # And keyword parameters
    for key, arg in kwargs.items():
        if arg is None:
            continue

        if key in parameters:
            raise ValueError('Multiple values for parameter %s supplied' % key)
        parameters[key] = smart_str(arg)

    parameters.update({
        'key': self.api.key,
        'version': self.api.version,
        'output': 'json',
    })

    url = urlparse.urlunparse(['http', self.api.host, self.path, None, urllib.urlencode(parameters), None])

    if self.api.cache:
        # TODO: really ugly code
        hash = hashlib.md5(url).hexdigest()
        try:
            # TODO: user must set root folder for cache
            os.makedirs('/tmp/2gis-cache')
        except OSError:
            pass
        filename = os.path.join('/tmp/2gis-cache/', hash)
        if os.path.exists(filename):
            return json.loads(open(filename).read())
        else:
            response = requests.get(url).json
            if response['response_code'] != '200':
                raise DgisError(response['response_code'], response['error_message'], response['error_code'])
            open(filename, 'w').write(json.dumps(response))

    else:
        response = requests.get(url).json
        if response['response_code'] != '200':
            raise DgisError(response['response_code'], response['error_message'], response['error_code'])

    # Register view if required
    if self.register_views and self.api.register_views:
        if requests.get(response['register_bc_url']).text == '0':
            raise DgisError(404, 'Firm\'s profile view registration cannot be processed', 'registerViewFailed')

    return response


def bind_api(**config):

    properties = {
        'path': config['path'],
        'method': config.get('method', 'GET'),
        'allowed_param': config['allowed_param'],
        'register_views': config.get('register_views', False),
        '__init__': __init__,
        'execute': execute,
    }

    cls = type('API%sMethod' % config['path'].title().replace('/', ''), (object,), properties)

    def _call(api, *args, **kwargs):
        return cls(api).execute(*args, **kwargs)

    return _call
