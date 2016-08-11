import socket
## Servidor Simples - By Viniicius Saw
HOST = ''
PORT = 5000
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
junto = (HOST, PORT)
conexao.bind(junto)
while True:
    msg, cliente = conexao.recvfrom(1024)
    print cliente, msg
conexao.close()
