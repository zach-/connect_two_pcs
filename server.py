import socket

sock = socket.socket()
print("Socket successfully created...")
host = socket.gethostname()
print("Socket created on: " + str(sock.getsockname()) + "...")
port = 26138
print("Opening port " + str(port) + " for communication...")
sock.bind((host, port))
sock.listen(5)
print(str(sock.getsockname()))
board = [2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("Server Started. Awaiting Connection....")
    c, address = sock.accept()
    print("Connection established from: " + repr(address[1]))
    # c.send("Connection established")
    c.send(str(board).strip("[]"))
    c.close()
