"""
Simple Server TCP/UDP
By Viniicius Saw
"""
import socket
HOST = ''
PORT = 5000
def udp():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conq = (HOST, PORT)
    connection.bind(conq)
    while True:
        msg, client = connection.recvfrom(1024)
        print(client, msg)
    connection.close()
def tcp():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conq = (HOST, PORT)
    connection.bind(conq)
    connection.listen(1)
    while True:
        icp, client = connection.accept()
        print('Connected from', client)
        while True:
            msg = con.recv(1024)
            if not msg: break
            print(client, msg)
        print('Disconnecting connection to client', client)
    connection.close()
select = int(raw_input(" #1 - UDP Server\n #2 - TCP Server\n -> "))
if select == 1:
    print('Started UDP Server')
    udp()
elif select == 2:
    print('Started TCP Server')
    tcp()
else:
    print('Invalid Option')
