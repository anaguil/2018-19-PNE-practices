import http.server
import socketserver
from seq_p6 import Seq

PORT = 8080


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        yes = True
        print("Path:", self.path)

        if self.path == "/" or self.path.startswith("/seq"):
            f = open("seq.html", 'r')
            contents = f.read()

        elif self.path.startswith("/echo"):
            list_message = self.path.split("&")
            sequence = list_message[0]
            i = sequence.find("?")
            sequence = sequence[i+5:].upper()
            for base in sequence.upper():
                if base != "A" and base != "C" and base != "G" and base != "T":
                    f = open("error.html")
                    contents = f.read()
                    yes = False
                    f.close()
            if yes == True:
                sequence = Seq(sequence)
                i_operation = self.path.find("operation=") + len("operation=")
                if 'chk' in self.path:
                    seq_len = sequence.len()
                    html_text_3 = """<p>Length: {}</p>""".format(seq_len)
                if 'count' in self.path:
                    j_operation = i_operation + len("count")
                    operation = self.path[i_operation:j_operation]
                    result_op = sequence.count(self.path[-1])
                if 'perc' in self.path:
                    j_operation = i_operation + len("perc")
                    operation = self.path[i_operation:j_operation]
                    result_op = sequence.perc(self.path[-1])

                html_text_1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Response</title>
    </head>
    <body>"""
                html_text_2 = """<p>Sequence: {}</p>""".format(sequence.strbases)
                html_text_4 = """<p>Operation and base requested: {}, {} </p>""".format(operation, self.path[-1])
                html_text_5 = """<p>Result of the operation: {}</p>""".format(result_op)
                html_text_6 = """</body></html>"""
                f = open("response-page.html", 'w')

                f.write(html_text_1 + html_text_2)
                if 'chk' in self.path:
                    f.write(html_text_3)
                f.write(html_text_4 + html_text_5 + html_text_6)
                f.close()

                f = open("response-page.html", 'r')
                contents = f.read()
                f.close()
        else:
            f = open("error_1.html", 'r')
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

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Stopped by the user")

print("The server is stopped")
