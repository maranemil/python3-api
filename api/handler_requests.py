from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

import middleware

"""
"http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing
ParseResult(scheme='http', netloc='docs.python.org:80',
            path='/3/library/urllib.parse.html', params='',
            query='highlight=params', fragment='url-parsing')
"""


def handler_request_get(url,self):
    parsed_url = urlparse(url)
    if parsed_url.path == '/api/register':
        response = middleware.register(url,self)
        if response:
            return {'message': 'Registration successful!'}
        else:
            return {'error': 'Registration failed.'}

    else:
        return {'error': 'Endpoint not found'}


def handler_request_post(url,self):
    parsed_url = urlparse(url)
    if parsed_url.path == '/api/login':
        response = middleware.login(url,self)
        if response:
            return {'message': 'Hello, login successful!'}
        else:
            return {'error': 'login failed.'}
    else:
        return {'error': 'Endpoint not found'}
