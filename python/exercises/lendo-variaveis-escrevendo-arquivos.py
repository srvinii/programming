#!/usr/bin/env python
# -*- encoding: utf-8 -*-
i = 1
dados = open('/home/vinii/Desktop/dados.txt', 'w')
while i <= 2:
    nome = raw_input("Diga seu nome: ")
    idade = raw_input("Digite sua idade: ")
    texto = "\nSeu nome e: " + nome + "\nSua idade e: " + idade
    dados.write(texto)
    texto = texto + "\n"
    i = i + 1
dados.close()
