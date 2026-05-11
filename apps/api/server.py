from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import json
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"OK"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/crash":
            os._exit(1)

        data = {
            "service": "api",
            "path": self.path,
            "hostname": socket.gethostname()
        }

        body = json.dumps(data, indent=2).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
