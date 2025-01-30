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
        
        # Complete marks data
        marks_data = {
            "r": 23, "LTHD": 79, "NudIVdiH": 96, "R4": 72, "S": 30,
            "jy1DITYE32": 52, "JrpT7YG": 88, "ef6AXyO": 89, "0IGO": 93,
            "o": 94, "06bW": 95, "Vs4bSIMU": 62, "nCU0HvE": 73, "Bfrq4": 42,
            "DZyyA": 35, "j": 87, "EkOAcHVo": 69, "n": 61, "A52wSm": 48,
            "qKFD": 79, "NYqMeJlpe": 76, "0nqeqojFz": 68, "U": 59, "s5Fh": 61,
            "i": 76, "g4s3phql8h": 76, "igdN02S": 68, "RhSy": 13, "ohqs": 89,
            "W": 10, "tubqV8L": 75, "f8": 57, "XGpFky": 53, "RBLmK9": 36,
            "V": 77, "aR0Nff6": 44, "Iewe4le": 21, "lmlb7VJ5": 8, "KFL45A": 11,
            "I2Pi7VGpm": 30, "fd": 24, "1hO9uh": 13, "z4wDhy": 58, "lZ": 19,
            "QHR": 8, "DWrNNE": 5, "BVxWLSmfrp": 20, "XyuHAStP": 11, "ZSuN1K": 61,
            "ak": 55, "t": 84, "1bF": 77, "vE": 40, "rKT9m4sI": 90, "MN": 29,
            "L0IeOMN": 18, "x": 64, "qpijdn1": 72, "C7": 50, "eVf": 95,
            "6IJg": 41, "PBeCK1g": 81, "mVayc": 51, "WlRP2TBF": 32, "JKi": 97,
            "EecMv": 55, "vFIhoFFO1G": 18, "5Xqlyfr6": 14, "vDGa": 47,
            "Z6WU": 52, "1w4FNT8Pg": 84, "Z9OWds3GDc": 28, "DfnyzipWFd": 21,
            "81TA9QZ2bE": 91, "THAk": 3, "0Zh": 29, "77W": 43, "h3NNh": 51,
            "e5": 79, "mdt3mOUniZ": 24, "rhE1tSvC": 79, "d": 40, "zvh": 53,
            "Lf3SzLy": 21, "6": 33, "8lZVrCno": 51, "PR1G4pAWL": 10,
            "fTlqSB5U9": 68, "1": 91, "sv": 27, "gmV9dl7P94": 12,
            "wxoOsO81sM": 57, "95T97pCca": 13, "Ac7AO3": 21, "8LlL": 73,
            "qoXh6IDO": 66, "zUsM1XDc": 74, "x": 64
        }
        
        # Get marks for requested names
        marks = [marks_data.get(name, 0) for name in names]
        
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))





