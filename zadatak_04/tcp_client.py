import socket
import selectors
import sys
import types

if len(sys.argv) < 3:
    exit(1)

SERVER_ADDR = sys.argv[1]
SERVER_PORT = int(sys.argv[2])

# Initialize socket to server

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setblocking(False)
server_socket.connect_ex((SERVER_ADDR, SERVER_PORT))

# Initialize selector

data = types.SimpleNamespace(header_sent=False,
                             content_sent_len=0)

sel = selectors.DefaultSelector()
sel.register(server_socket, selectors.EVENT_WRITE, data)

print("Input image path:")
img_path = input()

print("Input image title:")
img_title = input()

with open(img_path, "rb") as img_file:
    img_string = img_file.read()

payload = img_title.encode("utf-8") + img_string
# Main client loop

conn_ended = False
while not conn_ended:

    # Waiting for an event or terminate client
    try:
        events = sel.select(timeout=None) 
    except KeyboardInterrupt:

        sel.unregister(server_socket)
        server_socket.close()

        conn_ended = True
        continue
    
    # When event is registered
    for key, mask in events:
        
        server_socket = key.fileobj
        data = key.data

        if mask & selectors.EVENT_READ:
            print("Server socket is ready to read")
        if mask & selectors.EVENT_WRITE:
            print("Server socket is ready to write")

        if mask & selectors.EVENT_WRITE:  

            if not data.header_sent:

                header = f"{len(img_title):<8}{len(img_string):<8}"
                server_socket.sendall(header.encode("utf-8"))

                data.header_sent = True

            else:
                
                if data.content_sent_len < len(payload):

                    sent_len = server_socket.send(payload[data.content_sent_len:])
                    data.content_sent_len += sent_len

                else:
                    
                    print("Image sent")
                    conn_ended = True

            # sel.modify(serversocket, selectors.EVENT_READ, None)

        if mask & selectors.EVENT_READ:

            server_msg = server_socket.recv(1024)
            print(f"Server message: {server_msg.decode('utf-8')}")

            conn_ended = True

