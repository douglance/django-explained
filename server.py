#!/usr/bin/env python3
# Importing socket from the standard library
import socket

# Initialize the socket
s = socket.socket()

# Configure socket options
# SOL_SOCKET targets the socket layer
# SO_REUSEADDR says the socket can be reused
# 1 sets the SO_REUSEADDR to True
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# The port we want to use
# The range of ports is 16 bit unsigned integers: 0 - 65,535
PORT = 8080

# Tells our OS to route packets here
s.bind(("0.0.0.0", PORT))

# Activates the socket with a backlog of 10
s.listen(10)

# Our HTTP response
# the b converts the string to bytes
http_response = b"""\
HTTP/1.1 200 OK

Hello Taylor"""

# Prints out this message to the terminal
print(f'Server Running on port {PORT}')

# Endless loop to wait for a connection
while True:
    conn, address = s.accept()  # Request comes in
    # Receives the data from the request with buffer of 1024
    conn.recv(1024)
    conn.sendall(http_response)  # Sends the response
    conn.close()                # Closes connection

s.close()  # Closes socket

# curl localhost:8080 -v
