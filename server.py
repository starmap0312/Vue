import os
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.path == "/teacher":
                # http://localhost:9000/teacher
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write('[{"name": "John"}, {"name": "Tom"}]')
            else:
                # http://localhost:9000/hello_world.html
                with open(os.curdir + os.sep + self.path) as fout:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(fout.read())
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

try:
    print('Startint server at: {0}'.format('http://localhost:{0}'.format(9000)))
    server = HTTPServer(('', 9000), handler)
    print('Control+C to shutdown the server')
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
