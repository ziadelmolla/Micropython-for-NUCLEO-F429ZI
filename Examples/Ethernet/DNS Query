#Board must be connected to a router
#This code used for testing the Ethernet and communicate with the DNS server 


import network
import socket
nic = network.Ethernet()
nic.active(True)
nic.ifconfig('dhcp')
print(nic.ifconfig())
socket.getaddrinfo('micropython.org', 80)
