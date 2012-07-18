# -*- coding: utf-8 -*-


class DgisError(Exception):
    """2Gis API error"""

    def __init__(self, code, message, error_code):
        self.code = code
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return self.message
