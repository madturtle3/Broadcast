from socket import *
import ipaddress
s=socket(AF_INET, SOCK_DGRAM)
print(ipaddress.IPv4Network(gethostbyname(gethostname())).broadcast_address.__str__())
s.bind(("0.0.0.0",12345))
m=s.recvfrom(1024)
print(m)
