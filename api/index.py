from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Parse query parameters
        query_components = parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
        names = query_components.get('name', [])
        
        # Mock data for student marks
        marks = [10 if name == 'X' else 20 if name == 'Y' else 0 for name in names]
        
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))
