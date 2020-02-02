#!/usr/bin/env python3
import socket

# Initialize the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tells the socket that it can be reused
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# The port we want to use
PORT = 8080

# Tells OS to route packets here
s.bind(("0.0.0.0", PORT))

# Activates the socket
s.listen(10)

# Our response
http_response = b"""\
HTTP/1.1 200 OK

Hello, World!"""

print(f'Server Running on port {PORT}')
# Wait for a connection
while True:
    conn, address = s.accept()  # Request comes in
    conn.recv(1024)
    conn.sendall(http_response)        # Sends the response
    conn.close()                    # Closes connection

s.close()  # Closes socket

# curl localhost:8080 -v
