from http.server import BaseHTTPRequestHandler
from cowpy import cow
from covid import Covid

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        covid = Covid()
        covid = Covid(source="worldometers")
        cuba = covid.get_status_by_country_name("cuba")
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(cuba.encode())
        return

       



