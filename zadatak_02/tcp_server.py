import socket
import sys

if len(sys.argv) < 3:
    exit(1)

LISTEN_ADDR = sys.argv[1]
LISTEN_PORT = int(sys.argv[2])

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((LISTEN_ADDR, LISTEN_PORT))
listen_socket.listen()

server_running = True
while server_running:

    try:

        client_socket, address = listen_socket.accept()

    except KeyboardInterrupt:

        print("Exiting server...")

        listen_socket.close()
        server_running = False
        continue


    print(f"Client connected: {address}")

    msg = client_socket.recv(1024)
    print(f"Message from {address}: {msg.decode('utf-8')}")

    client_socket.sendall(bytes("Message received", "utf-8"))

    client_socket.close()

