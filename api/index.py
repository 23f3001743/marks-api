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
        
        # Updated marks data with the correct values
        marks_data = {
            "A": 14,
            "B": 11,
            "C": 36,
            "D": 79,
            "E": 66
        }
        
        # Get marks for requested names
        marks = [marks_data.get(name, 0) for name in names]
        
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))




