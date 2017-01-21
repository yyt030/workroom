#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

import os

from tornado import options, web


def create_app():
    options.define('port', default=8000, help='run on the given port', type=int)
    options.parse_command_line()
    app = web.Application(handlers=create_handlers(),
                          template_path=os.path.join(os.path.dirname(__file__), "templates"),
                          static_path=os.path.join(os.path.dirname(__file__), "static"),
                          debug=True)
    return app


def create_handlers():
    handlers = []
    from webapp.controllers.site import IndexHandler
    handlers.append((r"/", IndexHandler))
    return handlers
