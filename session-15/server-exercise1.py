import http.server
import socketserver

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("Path:", self.path)

        if self.path == "/" or self.path.endswith("form1.html"):
            f = open("form1.html", 'r')
            contents = f.read()

        elif self.path.startswith("/echo"):
            message = self.path
            i = message.find("=")
            message = message[i+1:]
            print(message)

            html_text_1 = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Response</title>
        </head>
        <body>
        <h1>Echo received:</h1>"""
            html_text_2 = """<p>{}</p>""".format(message)
            html_text_3 = """<p><a href="form1.html">[Main Page]</a></body></html>"""

            f = open("response-page.html", 'w')
            f.write(html_text_1 + html_text_2 + html_text_3)
            f.close()

            f = open("response-page.html", 'r')
            contents = f.read()
            f.close()

        else:
            f = open("error.html", 'r')
            contents = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # -- Sending the body of the response message
        self.wfile.write(str.encode(contents))



        return

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
