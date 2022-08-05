import socket
import sys

if len(sys.argv) < 2:
    exit(1)

SERVER_ADDR = sys.argv[1]
print(SERVER_ADDR)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_ADDR, 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
# new_msg = input()
# s.send(bytes(new_msg, "utf-8"))
