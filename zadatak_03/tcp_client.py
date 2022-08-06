import socket
import selectors
import sys

if len(sys.argv) < 3:
    exit(1)

SERVER_ADDR = sys.argv[1]
SERVER_PORT = sys.argv[2]

# Initialize socket to server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)
s.connect_ex((SERVER_ADDR, SERVER_PORT))

# Initialize selector

sel = selectors.DefaultSelector()
sel.register(s, selectors.EVENT_WRITE, None)

# Main client loop

conn_ended = False
while not conn_ended:

    # Waiting for an event or terminate client
    try:
        events = sel.select(timeout=None) 
    except KeyboardInterrupt:
        conn_ended = True
        continue
    
    # When event is registered
    for key, mask in events:
        
        serversocket = key.fileobj

        if mask & selectors.EVENT_READ:
            print("Server socket is ready to read")
        if mask & selectors.EVENT_WRITE:
            print("Server socket is ready to write")

        if mask & selectors.EVENT_WRITE:  

            msg = input()
            serversocket.sendall(bytes(msg, "utf-8"))

            sel.modify(serversocket, selectors.EVENT_READ, None)

        if mask & selectors.EVENT_READ:

            server_msg = serversocket.recv(1024)
            print(f"Server message: {server_msg.decode('utf-8')}")

            sel.unregister(serversocket)
            serversocket.close()

            comm_ended = True

