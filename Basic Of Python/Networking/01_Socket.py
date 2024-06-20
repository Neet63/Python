# Sockets are the endpoints of a bidirectional communications channel.

# Two type of communication :
# 1. Connection-Orienred -> TCP
# 2. Connectionless -> UDP

#sytex to create a socket
# socket.socket (socket_family, socket_type, protocol=0)


# Server Socket Methods
# bind() -> binds the socket to specified IP address and port number.
# listen() -> starts server and runs into a listen loop looking for connection request from client.
# accept() -> When connection request is intercepted by server, this method accepts it and identifies the client socket with its address.

#Example to create a socket
import socket
server = socket.socket()
server.bind(('localhost',80))
server.listen()
client, addr = server.accept()
print ("connection request from: " + str(addr))


