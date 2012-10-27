# -*- coding: utf-8 -*-

import six


def force_text(s, encoding='utf-8', errors='strict'):
    """
    Returns a bytestring version of 's', encoded as specified in 'encoding'.

    If strings_only is True, don't convert (some) non-string-like objects.

    Based on the `django.utils.encoding.smart_str' (https://github.com/django/django/blob/master/django/utils/encoding.py)
    """

    if not isinstance(s, six.string_types):
        try:
            return str(s)
        except UnicodeEncodeError:
            if isinstance(s, Exception):
                # An Exception subclass containing non-ASCII data that doesn't
                # know how to print itself properly. We shouldn't raise a
                # further exception.
                return ' '.join([force_text(arg, encoding, errors) for arg in s])
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, six.text_type):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s
