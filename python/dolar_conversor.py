# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def main():
	coins()

print '''
 ██████╗  ██████╗ ██╗      █████╗ ██████╗                                     
 ██╔══██╗██╔═══██╗██║     ██╔══██╗██╔══██╗                                    
 ██║  ██║██║   ██║██║     ███████║██████╔╝                                    
 ██║  ██║██║   ██║██║     ██╔══██║██╔══██╗                                    
 ██████╔╝╚██████╔╝███████╗██║  ██║██║  ██║                                    
 ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                    
                                                                            	
 ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ███████╗ ██████╗ ██████╗ 
 ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗
 ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝███████╗██║   ██║██████╔╝
 ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║   ██║██╔══██╗
 ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║███████║╚██████╔╝██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝

[*] Dolar Conversor v1.0
[*] Tool to convert dolar <> real
[*] Author: Eric Vinicius (\033[0;4mViniicius Saw\033[0m)                                                                    
'''

def coins():
	global url_real_to_dolar
	global url_dolar_to_real
	global url_dolar_to_eur
	global url_eur_to_dolar
	global url_eur_to_real
	global url_real_to_eur

	url_real_to_dolar = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=BRL'
	url_dolar_to_real = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=BRL&To=USD'
	url_dolar_to_eur = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR'
	url_eur_to_dolar = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD'
	url_eur_to_real = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=BRL'
	url_real_to_eur = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=BRL&To=EUR'
	connection()

def connection():
	header = {'user-agent': 'Mozilla\5.0 (Windows NT 10.0; Win64; x64) '
							'AppleWebKit/537.36 (KHTML, like Gecko) '
							'Chrome/51.0.2704.103 Safari/537.36'}
	# ---------------- Req real to dolar ----------------
	req_real_to_dolar = requests.get(url_real_to_dolar, headers=header)
	soup_dolar = BeautifulSoup(req_real_to_dolar.text, 'html.parser')
	dolar_to_real = soup_dolar.find(class_="uccResultAmount")
	dolar_to_real_value = dolar_to_real.get_text()
	global dolar_to_real_float
	dolar_to_real_float = float(dolar_to_real_value)
	# ---------------- Req dolar to real ----------------
	req_dolar_to_real = requests.get(url_dolar_to_real, headers=header)
	soup_real = BeautifulSoup(req_dolar_to_real.text, 'html.parser')
	real_to_dolar = soup_real.find(class_="uccResultAmount")
	real_to_dolar_value = real_to_dolar.get_text()
	global real_to_dolar_float
	real_to_dolar_float = float(real_to_dolar_value)
	# ---------------- Req dolar to euro ----------------
	req_dolar_to_eur = requests.get(url_dolar_to_eur, headers=header)
	soup_eur = BeautifulSoup(req_dolar_to_eur.text, 'html.parser')
	dolar_to_eur = soup_eur.find(class_="uccResultAmount")
	dolar_to_eur_value = dolar_to_eur.get_text()
	global dolar_to_eur_float
	dolar_to_eur_float = float(dolar_to_eur_value)
	# ---------------- Req euro to dolar ----------------
	req_eur_to_dolar = requests.get(url_eur_to_dolar, headers=header)
	soup_eur = BeautifulSoup(req_eur_to_dolar.text, 'html.parser')
	eur_to_dolar = soup_eur.find(class_="uccResultAmount")
	eur_to_dolar_value = eur_to_dolar.get_text()
	global eur_to_dolar_float
	eur_to_dolar_float = float(eur_to_dolar_value)
	# ---------------- Req euro to real ----------------
	req_eur_to_real = requests.get(url_eur_to_real, headers=header)
	soup_real = BeautifulSoup(req_eur_to_real.text, 'html.parser')
	eur_to_real = soup_real.find(class_="uccResultAmount")
	eur_to_real_value = eur_to_real.get_text()
	global eur_to_real_float
	eur_to_real_float = float(eur_to_real_value)
	# ---------------- Real euto to euro ----------------
	req_real_to_eur = requests.get(url_real_to_eur, headers=header)
	soup_real = BeautifulSoup(req_real_to_eur.text, 'html.parser')
	real_to_eur = soup_real.find(class_="uccResultAmount")
	real_to_eur_value = real_to_eur.get_text()
	global real_to_eur_float
	real_to_eur_float = float(real_to_eur_value)


	alternatives()

def conversor(type_coin, select):
	if type_coin == 1:
		if select == 1:
			conversion = float(input('\nValue to convert: '))
			result = dolar_to_real_float * conversion
			print '%d USD = %.3f BRL' %(conversion, result)
		elif select == 2:
			conversion = float(input('\nValue to convert: '))
			result = dolar_to_eur_float * conversion
			print '%d USD = %.3f EUR' %(conversion, result)

	elif type_coin == 2:
		if select == 1:
			conversion = float(input('\nValue to convert: '))
			result = eur_to_dolar_float * conversion
			print '%d EUR = %.3f USD' %(conversion, result)
		elif select == 2:
			conversion = float(input('\nValue to convert: '))
			result = eur_to_real_float * conversion
			print '%d EUR = %.3f BRL' %(conversion, result)
	elif type_coin == 3:
		if select == 1:
			conversion = float(input('\nValue to convert: '))
			result = real_to_dolar_float * conversion
			print '%d BRL = %.3f USD' %(conversion, result)
		elif select == 2:
			conversion = float(input('\nValue to convert: '))
			result = real_to_eur_float * conversion
			print '%d BRL = %.3f EUR' %(conversion, result)
		else:
			print 'Option no exists'

def alternatives():
	global select
	type_coin = 0
	print '1) Dolar (USD)'
	print '2) Euro (EUR)'
	print '3) Real (BRL)'
	option = input('\nOption: ')
	if option == 1:
		type_coin = 1
		print '\n'
		print '1) Dolar -> Real'
		print '2) Dolar -> Euro'
		select = input('\nOption: ')
		conversor(type_coin, select)
	elif option == 2:
		type_coin = 2
		print '\n'
		print '1) Euro -> Dolar'
		print '2) Euro -> Real'
		select = input('\nOption: ')
		conversor(type_coin, select)
	elif option == 3:
		type_coin = 3
		print '\n'
		print '1) Real -> Dolar'
		print '2) Real -> Euro'
		select = input('\nOption: ')
		conversor(type_coin, select)
	else:
		print 'Option no exists'
main()