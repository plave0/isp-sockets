import socket
import sys

if len(sys.argv) < 3:
    exit(1)

SERVER_ADDR = sys.argv[1]
PORT = int(sys.argv[2])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_ADDR, 1234))

msg = input()
server_socket.sendall(bytes(msg, "utf-8"))

server_msg = server_socket.recv(1024)
print(f"Server message: {server_msg.decode('utf-8')}")
