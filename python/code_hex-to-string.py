#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Autor: Eric Vinicius (Vinicius Saw)
# Programa simples apenas com o de incentivar o estudo da linguagem :D
###############################################################
def codificar(str_normal):
    str_hex = str_normal.encode('hex')
    return(str_hex)
def decodificar(str_normal):
    str_hex = str_normal.decode('hex')
    return(str_hex)
opcao = 1
while opcao == 1:
    print "  \n\nPrograma Str <> Hex - Eric Vinicius"
    valor = int(input("\n 1 - String -> Hex\n 2 - Hex -> String\n 3 - Sair\n\n Fazer: "))
    if valor == 1:
        str_normal = raw_input("\n\nInsira a string:\n")
        print "String codificada: ", codificar(str_normal)
    if valor == 2:
        str_normal = raw_input("\n\nInsira a string:\n")
        print "String decodificada: ", decodificar(str_normal)
    if valor == 3:
        exit()
    elif valor != 1 and valor != 2 and valor != 3:
        print "Opção Incorreta"

