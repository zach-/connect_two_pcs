import socket

sock = socket.socket()
host = socket.gethostname()
port = 26138
sock.bind((host, port))
sock.listen(5)

while True:
    print("Server Started. Awaiting Connection....")
    c, address = sock.accept()
    print("Connection established from: " + repr(address[1]))
    c.send("Connection established")
    c.close()
