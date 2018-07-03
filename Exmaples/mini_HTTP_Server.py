# This code implements a server on the boards, the user can send HTTP get requests with the command to be executed in the path,the 
# board will receive the command and execute it. Ex "http://192.168.1.6/pyb.LED(1).on()"


import network
import usocket as socket
import re

nic = network.Ethernet()
nic.active(1)
nic.ifconfig(('192.168.1.6','255.255.255.0','192.168.1.1','8.8.8.8'))
s = socket.socket()
s.bind(('192.168.1.6', 80))
s.listen(1)
while True:
	conn, addr = s.accept()
	txt = conn.recv(512)
	m=re.search('/(.+?) HTTP/',txt)
	cmd = m.group(1)
	exec(cmd)
