# -*- coding: utf-8 -*-
class Conta(object):
	
	def __init__(self, usuario, saldo):
		self.usuario = usuario
		self.saldo = saldo
	
	def depositar(self, reais):
		if reais > 0:
			self.saldo = self.saldo + reais
			print "\033[0;32mDepósito de R$ %.2f realizado com sucesso!\033[0m"%reais
		else:
			print "Você não pode depositar este valor"
	
	def sacar(self, reais):
		if reais > self.saldo:
			print "Saldo insuficiente"
		else:
			self.saldo = self.saldo - reais
			print "\033[0;31mSaque de R$ %.2f realizado com sucesso!\033[0m"%reais
