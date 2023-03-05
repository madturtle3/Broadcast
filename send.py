import socket
import socklib
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",12345))
server.listen(0)
message_string = "LIGHTER_INIT"
sock.sendto(message_string.encode(),('<broadcast>',12345))
conn,addr = server.accept()
socklib.send(conn,[0]*64)