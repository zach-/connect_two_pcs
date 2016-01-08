import socket

s = socket.socket()
host = raw_input('Enter the ipv4 address of the client: ')
port = 26138
s.connect((host, port))
print s.recv(1024)
