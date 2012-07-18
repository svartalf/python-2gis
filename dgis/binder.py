# -*- coding: utf-8 -*-

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

    # TODO: Catch HTTP errors
    # TODO: check for `response_code` key
    response = requests.get(url).json
    if response['response_code'] != '200':
        raise DgisError(response['response_code'], response['error_message'], response['error_code'])

    return response


def bind_api(**config):

    properties = {
        'path': config['path'],
        'method': config.get('method', 'GET'),
        'allowed_param': config['allowed_param'],
        '__init__': __init__,
        'execute': execute,
    }

    cls = type('APIMethod', (object,), properties)

    def _call(api, *args, **kwargs):
        return cls(api).execute(*args, **kwargs)

    return _call
