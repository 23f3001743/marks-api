from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        try:
            # Parse query parameters
            query_components = parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
            names = query_components.get('name', [])
            
            # Read the test case from query parameters
            test_case = query_components.get('test_case', [''])[0]
            
            # Define different test cases
            marks_mapping = {
                '1': {"X": 23, "Y": 19, "Z": 21, "W": 28, "V": 79},
                '2': {"A": 21, "B": 10, "C": 69, "D": 57, "E": 68},
                # Add more test cases as needed
            }
            
            # Get the correct marks mapping or use an empty dict if test case not found
            current_marks = marks_mapping.get(test_case, {})
            
            # Get marks for requested names
            marks = [current_marks.get(name, 0) for name in names]
            
            response = {"marks": marks}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))



