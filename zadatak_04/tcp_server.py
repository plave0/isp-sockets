import socket
import selectors 
import sys
import types
import io
from PIL import Image

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

            data = types.SimpleNamespace(addr=address,
                                         header_received=False,
                                         title_len=0,
                                         img_len=0,
                                         img_content=b'')

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

                if not data.header_received:

                    msg = clientsocket.recv(16)

                    data.header_received = True
                    data.title_len = int(msg[:5].decode("utf-8"))
                    data.img_len = int(msg[5:].decode("utf-8"))
                    
                    print(f"Header received from {data.addr}")
                    print(f"Img size: {data.img_len}")

                elif len(data.img_content) < data.img_len + data.title_len:
                    
                    msg = clientsocket.recv(1024)
                    print(f"Bytes read: {len(msg)}")

                    if msg:
                        data.img_content += msg

                    print(f"Total bytes read: {len(data.img_content)}")
                    print(f"Total payload size: {data.img_len + data.title_len}")

                else:
                    
                    sel.unregister(clientsocket)

                    title = data.img_content[:data.title_len].decode("utf-8")
                    img = Image.open(io.BytesIO(data.img_content[data.title_len:]))
                    
                    print(f"Image title: {title}")
                    img.show()
                
            if mask & selectors.EVENT_WRITE:                

                clientsocket.sendall(bytes("Message received", "utf-8"))
                print(f"Connection ended: {data.addr}") 

                sel.unregister(clientsocket)

# End of server main loop -> exiting server

print("Exiting server...")
listen_socket.close()
sel.unregister(listen_socket)

