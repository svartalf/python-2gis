# -*- coding: utf-8 -*-

import inspect
try:
    import urlparse
except ImportError:  # Python 3
    from urllib import parse as urlparse
try:
    from urllib import urlencode
except ImportError:  # Python 3
    from urllib.parse import urlencode

import requests

from dgis.exceptions import DgisError
from dgis.utils import force_text

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
            parameters[self.allowed_param[idx]] = force_text(arg)
        except IndexError:
            raise ValueError('Too many parameters supplied')

    # And keyword parameters
    for key, arg in kwargs.items():
        if arg is None:
            continue

        if key in parameters:
            raise ValueError('Multiple values for parameter %s supplied' % key)
        parameters[key] = force_text(arg)

    parameters.update({
        'key': self.api.key,
        'version': self.api.version,
        'output': 'json',
    })

    url = urlparse.urlunparse(['http', self.api.host, self.path, None, urlencode(parameters), None])

    response = requests.get(url).json
    if inspect.ismethod(response):
        response = response()

    if response['response_code'] != '200':
        raise DgisError(int(response['response_code']), response['error_message'], response['error_code'])

    # Register view if required
    if self.register_views and self.api.register_views:
        if requests.get(response['register_bc_url']).text == '0':
            raise DgisError(404, 'View registration cannot be processed', 'registerViewFailed')

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
