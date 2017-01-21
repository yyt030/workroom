#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

from tornado import httpserver, ioloop

from webapp import create_app
from webapp import options

app = create_app()

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.options.port)
    print('app server[port:{:d}] starting  ... '.format(options.options.port))

    ioloop.IOLoop.instance().start()
