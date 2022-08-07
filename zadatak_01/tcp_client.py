import socket
import sys

if len(sys.argv) < 3:
    exit(1)

SERVER_ADDR = sys.argv[1]
PORT = int(sys.argv[2])

# Connecting to the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_ADDR, PORT))

# Recieve message form server
msg = server_socket.recv(1024)
print(msg.decode("utf-8"))

