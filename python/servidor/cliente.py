import socket
## Cliente Simples - By Viniicius Saw
HOST = ''
PORT = 5000
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
junto = (HOST, PORT)
print 'Ctrl + X para sair'
msg = raw_input()
while msg <> '\x18':
    conexao.sendto(msg, junto)
    msg = raw_input()
conexao.close()
