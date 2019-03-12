import http.server
import socketserver
import termcolor

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # -- Printing the request line
        termcolor.cprint(self.requestline, 'green')

        f = open("form1.html", 'r')
        contents = f.read()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))


# -- Main program
# Empty address means that it is your own (localhost)

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Stopped by the user")

print("The server is stopped")
