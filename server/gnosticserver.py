from http.server import BaseHTTPRequestHandler, HTTPServer
from .handler import posthandler

class GnosticRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            posthandler(self.rfile)
        except Exception as e:
            self.send_response_only(500, str(e))
        else:
            self.send_response_only(200, "Success")



