import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object called client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# using the sendto() method, send some data to the IP and port using the client object
client.sendto(b"AAABBBCCC",(target_host,target_port))

# put the received data into the variables data and addr
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()