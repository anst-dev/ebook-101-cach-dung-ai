#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web-reader")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' not found. Please run scripts/build_web_data.py first.")
        sys.exit(1)
        
    # Standard server startup
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n=======================================================")
        print(f" Ebook Reader Server is running!")
        print(f" Open your browser and go to: http://localhost:{PORT}")
        print(f"=======================================================\n")
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")
            sys.exit(0)

if __name__ == "__main__":
    main()
