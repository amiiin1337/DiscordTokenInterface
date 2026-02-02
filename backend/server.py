import http.server
import json
import threading
from automation import discord_login_with_token

PORT = 8000

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                token = data.get('token')
                
                if token:
                    # Run automation in a separate thread to not block the server
                    thread = threading.Thread(target=discord_login_with_token, args=(token,))
                    thread.daemon = True # Allow server to exit even if thread is running
                    thread.start()
                    
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*') # Allow CORS for local testing
                    self.end_headers()
                    self.wfile.write(json.dumps({'status': 'success', 'message': 'Automation started'}).encode('utf-8'))
                else:
                    self.send_error(400, "Token missing")
            except json.JSONDecodeError:
                self.send_error(400, "Invalid JSON")
        else:
            self.send_error(404)

    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

print(f"Server running on http://localhost:{PORT}")
http.server.HTTPServer(('', PORT), RequestHandler).serve_forever()
