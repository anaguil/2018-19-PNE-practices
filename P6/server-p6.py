import http.server
import socketserver
from seq import Seq

PORT = 8080

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("Path:", self.path)

        if self.path == "/" or self.path.startswith("/seq"):
            f = open("seq.html", 'r')
            contents = f.read()

        elif self.path.startswith("/echo"):
            message = self.path
            i = message.find("=")
            message = message[i + 1:]
            for base in message.upper():
                if base != "A" and base != "C" and base != "G" and base != "T":
                    f = open("error.html")
                    contents = f.read()
                else:
                    ######

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))

        return


# -- Main program

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Stopped by the user")

print("The server is stopped")