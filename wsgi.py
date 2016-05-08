#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mxreverse import application as mxreverse
from whitenoise import WhiteNoise
from wsgiref.util import shift_path_info


def app(environ, start_response):
    path = shift_path_info(environ)
    print(path)
    if path == 'api':
        return mxreverse(environ, start_response)
    start_response('301 Moved', [('Location', '/page/index.html')])
    return [b'']


application = WhiteNoise(app, root='page', prefix='page')
