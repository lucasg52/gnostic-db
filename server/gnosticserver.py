from http.server import BaseHTTPRequestHandler, HTTPServer
from .handler import PostHandler

class GnosticRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            handler = PostHandler(self.rfile)
        except Exception as e:
            self.send_response_only(500, str(e))
        else:
            self.send_response_only(200, "Success")

        print(handler.metadata)



