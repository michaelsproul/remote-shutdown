import http.server
import socketserver
import subprocess

from http.server import SimpleHTTPRequestHandler
from subprocess import Popen

PORT = 80

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/shutdown/":
            self.wfile.write("HTTP/1.1 200 OK\n\nShutting down...".encode())
            self.send_response(200)
            subprocess.Popen(["shutdown", "-h", "now"]).wait()
        else:
            SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.TCPServer(("", PORT), RequestHandler)
httpd.serve_forever()
