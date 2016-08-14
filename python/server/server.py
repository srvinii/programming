# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Simple Server TCP/UDP
By Viniicius Saw
"""

from sys import platform
from os import system
import argparse
import socket

gray = "\033[0;37m"
green = "\033[0;32m"
red = "\033[0;31m"
default = "\033[0m"

try:
    raw_input
except NameError:
    raw_input = input

def os():
    if platform == "linux" or platform == "linux2":
        system('clear')
    elif platform == "win32":
        system('cls')
    else:
        pass

os()

parser = argparse.ArgumentParser()
parser.add_argument("--host", action="store", dest="host", help="add a host")
parser.add_argument("--port", action="store", dest="port", help="add a port")
parser.add_argument("--type", action="store", dest="type", help="type to connection")
args = parser.parse_args()
def udp():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        conq = (str(args.host), int(args.port))
        connection.bind(conq)
    except OSError:
        print("[-] Endereço ", red, args.host, default, " não encontrado")
        exit()
    while True:
        msg, client = connection.recvfrom(1024)
        print(client, msg)
    connection.close()
def tcp():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conq = (str(args.host), int(args.port))
        connection.bind(conq)
    except OSError:
        print("[-] Endereço ", red, args.host, default, " não encontrado")
        exit()
    connection.listen(1)
    while True:
        icp, client = connection.accept()
        print('Connected from', client)
        while True:
            msg = conq.recv(1024)
            if not msg: break
            print(client, msg)
        print('Disconnecting connection to client', client)
    connection.close()
if args.type == "udp":
    print(gray, 'UDP server started in ',green, args.host, default)
    udp()
elif args.type == "tcp":
    print(gray, 'TCP server started in ',green, args.host, default)
    tcp()
else:
    print(red, 'Invalid Option', default)
