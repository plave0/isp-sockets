import socket
import sys

if len(sys.argv) < 2:
    exit(1)

LISTEN_ADDR = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((LISTEN_ADDR, 1234))

while True:

    s.listen(5)

    clientsocket, address = s.accept()
    with clientsocket:

        print(f"Client connected: {address}")

        msg = clientsocket.recv(1024)
        print(f"Client message: {msg.decode('utf-8')}")

        clientsocket.sendall(bytes("Message received", "utf-8"))

    clientsocket.close()

