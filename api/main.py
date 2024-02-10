from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging

import handler_requests


class SimpleHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, response_body):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_body).encode('utf-8'))

    def do_GET(self):
        print("MY SERVER: I got a GET request.")
        if self.path != '/':
            if self.path == '/api':
                response_body = {'message': 'Hello, this is your API!'}
                self._send_response(200, response_body)
            else:
                response_body = handler_requests.handler_request_get(self.path, self)
                self._send_response(200, response_body)
        else:
            self._send_response(404, {'error': 'Endpoint not found'})

    def do_POST(self):

        if self.path != '/':
            if self.path == '/api':
                response_body = {'message': 'Hello, this is your API!'}
                self._send_response(200, response_body)
            else:
                response_body = handler_requests.handler_request_post(self.path, self)
                self._send_response(200, response_body)
        else:
            self._send_response(404, {'error': 'Endpoint not found'})


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
