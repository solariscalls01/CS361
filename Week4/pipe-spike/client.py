# Echo Client side

import socket

# create the server and port number to allow connection between the server and the client
HOST = "localhost"
PORT = 3000

# Uses TCP socket binding
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Convert the bytes data to a message string to be decoded and encoded
    data = (b"A message from CS361!")
    data_str = data.decode('utf-8')
    s.sendall(data_str.encode('utf-8'))

# send the encoded string data back to server
print(f'Sent data: "{data_str}"')
s.close()
