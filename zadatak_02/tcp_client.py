import socket
import sys

if len(sys.argv) < 2:
    exit(1)

SERVER_ADDR = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_ADDR, 1234))

    msg = input()
    s.sendall(bytes(msg, "utf-8"))
    server_msg = s.recv(1024)

print(f"Server message: {server_msg.decode('utf-8')}")
