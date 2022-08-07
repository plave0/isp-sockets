import socket
import selectors
import sys

if len(sys.argv) < 3:
    exit(1)

SERVER_ADDR = sys.argv[1]
SERVER_PORT = int(sys.argv[2])

# Initialize socket to server

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setblocking(False)
server_socket.connect_ex((SERVER_ADDR, SERVER_PORT))

# Initialize selector

sel = selectors.DefaultSelector()
sel.register(server_socket, selectors.EVENT_WRITE, None)

# Main client loop

client_running = True
while client_running:

    # Waiting for an event or terminate client
    try:

        events = sel.select(timeout=None) 

    except KeyboardInterrupt:
        
        print("Exiting client...")

        client_running = False
        
        sel.unregister(server_socket)
        server_socket.close()

        continue
    
    # When event is registered
    for key, mask in events:
        
        server_socket = key.fileobj

        if mask & selectors.EVENT_READ:
            print("Server socket is ready to read")
        if mask & selectors.EVENT_WRITE:
            print("Server socket is ready to write")

        if mask & selectors.EVENT_WRITE:  

            msg = input()
            server_socket.sendall(bytes(msg, "utf-8"))

            sel.modify(server_socket, selectors.EVENT_READ, None)

        if mask & selectors.EVENT_READ:

            server_msg = server_socket.recv(1024)
            print(f"Server message: {server_msg.decode('utf-8')}")

            sel.unregister(server_socket)
            server_socket.close()

            client_running = False
