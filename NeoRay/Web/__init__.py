#   _  _         ___           
#   | \| |___ ___| _ \__ _ _  _ 
#   | .` / -_) _ \   / _` | || |
#   |_|\_\___\___/_|_\__,_|\_, |
#                           |__/ 
#
#   NeoRay Web Server by CodCatDev

import os
from socket import socket, AF_INET, SOCK_STREAM

class RunServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # run
        _Server(self).start()

class _Server:
    def __init__(self, self2: RunServer):
        self.host = self2.host
        self.port = self2.port

    def check(self):
        if not os.path.exists('www'):
            os.mkdir('www')
        if not os.path.exists('www/index.html'):
            with open('www/index.html', 'w') as f:
                f.write("<html><body><h1>Hello, World!222</h1></body></html>")

    def start(self):
        self.check()
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            resp = 
            # resp = (
            #    "HTTP/1.1 200 OK\r\n"
            #    "Content-Type: text/html; charset=utf-8\r\n"
            #    f"Content-Length: {len(response_body)}\r\n"
            #    "Connection: close\r\n"
            #    "\r\n"
            #    f"{response_body}"
            #)
            conn.sendall(resp.encode('utf-8'))
