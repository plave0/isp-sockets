import socket
import selectors
import sys
import types

if len(sys.argv) < 3:
    exit(1)

LISTEN_ADDR = sys.argv[1]
LISTEN_PORT = int(sys.argv[2])

# Initialize listening socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listen_socket.bind((LISTEN_ADDR, LISTEN_PORT))
listen_socket.listen()
listen_socket.setblocking(False)

# Initialize selector

sel = selectors.DefaultSelector()
sel.register(listen_socket, selectors.EVENT_READ, data = None)

# Main server loop

server_running = True
while server_running:
   
    # Waiting for an event or terminate server
    try:
        events = sel.select(timeout=None)
    except KeyboardInterrupt:
        server_running = False
        continue

    # When event is registered
    for key, mask in events:

        if key.data is None: # A new client has connected

            # Accepting the connection

            clientsocket, address = listen_socket.accept()
            clientsocket.setblocking(False)

            data = types.SimpleNamespace(addr=address)
            sel.register(clientsocket, selectors.EVENT_READ, data=data)

            print(f"Client connected: {address}") 
            
        else: # A client that is already connect has triggered an event

            # Responding to client

            clientsocket = key.fileobj
            data = key.data
            
            if mask & selectors.EVENT_READ:
                print("Client socket is ready to read")
            if mask & selectors.EVENT_WRITE:
                print("Client socket is ready to write")

            if mask & selectors.EVENT_READ:

                msg = clientsocket.recv(1024)
                print(f"Message received from {data.addr}: {msg.decode('utf-8')}")

                sel.modify(clientsocket, selectors.EVENT_WRITE, data)
                
            if mask & selectors.EVENT_WRITE:                

                clientsocket.sendall(bytes("Message received", "utf-8"))
                print(f"Connection ended: {data.addr}") 

                sel.unregister(clientsocket)

# End of server main loop -> exiting server

print("Exiting server...")
listen_socket.close()
sel.unregister(listen_socket)

