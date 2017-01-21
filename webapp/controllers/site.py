#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

from tornado import web


class IndexHandler(web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')
