import socket
import sys

if len(sys.argv) < 2:
    exit(1)

LISTEN_ADDR = sys.argv[1]

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((LISTEN_ADDR, 1234))
    s.listen(5)


    clientsocket, address = s.accept()
    clientsocket.send(bytes("Dobrodosao na server!", "utf-8"))
    print(f"Client connected: {address}")

    s.close()

