import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHTTPServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        print('Request:', self.path)
        self.send_response(200)

        self.send_header('Content-Type', 'application-json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        texte = open('file.json', 'r').read()
        self.wfile.write(texte.encode())

def tester(HandlerClass=MyHTTPServer,
         ServerClass=HTTPServer, protocol="HTTP/1.0", port=8002, bind=""):
    """Test the HTTP request handler class.

    This runs an HTTP server on port 8002 (or the port argument).

    """
    server_address = (bind, port)

    HandlerClass.protocol_version = protocol
    with ServerClass(server_address, HandlerClass) as httpd:
        sa = httpd.socket.getsockname()
        serve_message = "Serving HTTP on {host} port {port} (http://{host}:{port}/) ..."
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            sys.exit(0)

tester()