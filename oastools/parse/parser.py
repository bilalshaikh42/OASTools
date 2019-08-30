""" parser

:Author: Bilal Shaikh < bilalshaikh42@gmail.com >
:Date: 2019-08-29
:Copyright: 2019, Bilal Shaikh
:License: MIT
"""
from .. import utils
import os.path


class OpenApiParser(object):
    def __init__(self, path=None):
        self.spec = utils.parse_file(path)
