import socket
import socklib
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",12345))
m=s.recvfrom(1024)
if m[0] == b"LIGHTER_INIT":
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((m[1][0],12345))
    message = socklib.recv(connection)
    print(message)