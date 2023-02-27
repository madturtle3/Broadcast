import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
message_string = "IP_SERVER_LIGHTER"
sock.sendto(message_string.encode(),('<broadcast>',12345))