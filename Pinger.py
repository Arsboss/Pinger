from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # определяем метод `do_GET` 
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Wait pls')
        subprocess.call(['sh', './Ping.sh'])



httpd = HTTPServer(('localhost', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()
