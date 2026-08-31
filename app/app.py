from http.server import BaseHTTPRequestHandler, HTTPServer
import os

VERSION = os.getenv("VERSION", "v8")


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if self.path == "/version":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(VERSION.encode())
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        response = f"PRODUCT VERSION V7-PILOT-CANARY {VERSION}\n"
        self.wfile.write(response.encode())


server = HTTPServer(("0.0.0.0", 8080), Handler)

print(f"Starting PRODUCT application version {VERSION}")

server.serve_forever()
