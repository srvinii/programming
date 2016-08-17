import argparse
import socket
from os import system
import sys,platform

green = "\033[0;32m"
red = "\033[0;31m"
default = "\033[0m"
gray = "\033[0;37m"

def main():
	#os()
	lg()
	arguments()
	connect()

def os():
	if sys.platform == 'linux' or sys.platform == 'linux2':
		system('clear')
	if sys.platform == 'win32':
		system('cls')
	else:
		pass

def lg():
	print('''
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|                                   

''')

def arguments():
	global args
	parser = argparse.ArgumentParser()
	print('Welcome to Vinicius PortScan!')
	print('Uses -h or --help to consult commands.')
	parser.add_argument("-i", dest="host", action="store", help="Uses -h to set a host. Ex: %(prog)s -i www.google.com")
	parser.add_argument("-p", dest="port", action="store", help="Uses -p to set a port to scan. Ex: %(prog)s -p 80")
	args = parser.parse_args()

def connect():
	if(args.host and args.port):
		print('Target: ', gray, args.host, default)
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.settimeout(2)
		icp = connection.connect_ex((str(args.host),int(args.port)))
		if icp == 0:
			print('Port', gray, args.port, green, 'Open', default)
		else:
			print('Port', gray, args.port, red, 'Close', default)
	else:
		exit()
main()