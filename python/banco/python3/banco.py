# -*- coding: utf-8 -*-
from conta import Conta

try:
	raw_input
except NameError:
	raw_input = input

usuario = raw_input("Proprietário da conta: ")
saldo = float(raw_input("Saldo do proprietário: "))

conta_usuario = Conta(usuario, saldo)

while True:
	print("""
	1) Consultar saldo atual
	2) Realizar depósito
	3) Realizar saque
	""")

	escolha = raw_input("\033[0;36m Escolha: \033[0m")

	if escolha == '1':
		print("Saldo Atual: \033[0;33m R$ %.2f\033[0m\n\n"%conta_usuario.saldo)
	
	elif escolha == '2':
		deposito = float(raw_input("Valor a ser depositado: \033[0;32m"))
		print("\033[0m")
		conta_usuario.depositar(deposito)
	
	elif escolha == '3':
		saque = float(raw_input("Valor a ser sacado: \033[0;31m"))
		print("\033[0m")
		conta_usuario.sacar(saque)
