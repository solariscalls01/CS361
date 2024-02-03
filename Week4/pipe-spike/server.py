# Echo Server Side

import socket

# create the server and port number to allow connection between the server and the client
address = ('localhost', 3000)

# create the TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(address) # bind the address to the TCP socket
server_socket.listen(3)     # allows for u up to 3 connections to listen

print(f"Server listening on {address[0], address[1]}")

while True:
    print("Waiting for connection\n")
    conn, addr = server_socket.accept()

    print(f'{addr} established')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received: ", data.decode('utf-8'))

    # close the socket once all data has been received
    print(f'Data has been received. \nClosing connection at {addr}')
    conn.close()
    break