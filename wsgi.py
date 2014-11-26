#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mxreverse import application as mxreverse
from static import Cling
from wsgiref.util import shift_path_info


page = Cling('page')


def application(environ, start_response):
    path = shift_path_info(environ)
    if path == 'api':
        return mxreverse(environ, start_response)
    elif path == 'page':
        return page(environ, start_response)
    start_response('301 Moved', [('Location', '/page')])
    return [b'']
