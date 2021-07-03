import socket

target_host = '127.0.0.1'
target_port = 9998

# create a socket object called client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# call the connect() method and connect the client object
client.connect((target_host,target_port))

# call the send() method and send some data to the client object
client.send(b"Test, hello there!\r\n\r\n")
response = client.recv(4096)

print(response.decode())
client.close()