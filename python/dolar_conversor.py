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
	global url_to_dolar
	global url_to_real
	url_to_dolar = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=BRL'
	url_to_real = 'http://www.xe.com/currencyconverter/convert/?Amount=1&From=BRL&To=USD'
	connection()

def connection():
	header = {'user-agent': 'Mozilla\5.0 (Windows NT 10.0; Win64; x64) '
							'AppleWebKit/537.36 (KHTML, like Gecko) '
							'Chrome/51.0.2704.103 Safari/537.36'}

	req_to_dolar = requests.get(url_to_dolar, headers=header)
	req_to_real = requests.get(url_to_real, headers=header)

	soup_dolar = BeautifulSoup(req_to_dolar.text, 'html.parser')
	soup_real = BeautifulSoup(req_to_real.text, 'html.parser')

	dolar_to_real = soup_dolar.find(class_="uccResultAmount")
	dolar_to_real_value = dolar_to_real.get_text()
	dolar_to_real_float = float(dolar_to_real_value)

	real_to_dolar = soup_real.find(class_="uccResultAmount")
	real_to_dolar_value = real_to_dolar.get_text()
	real_to_dolar_float = float(real_to_dolar_value)
	alternatives(dolar_to_real_float, real_to_dolar_float)

def conversor(conversion, dolar_to_real_float, real_to_dolar_float):
	if select == 1:
		result = dolar_to_real_float * conversion
		print '%d USD = %.3f BRL' %(conversion, result)
	elif select == 2:
		result = real_to_dolar_float * conversion
		print '%d BRL = %.3f USD' %(conversion, result)
	else:
		print 'Option no exists'

def alternatives(dolar_to_real_float, real_to_dolar_float):
	print '1) Dolar -> Real'
	print '2) Real  -> Dolar'
	global select
	select = input('\nSay 1 or 2: ')
	conversion = float(input('\nValue to convert: '))
	conversor(conversion, dolar_to_real_float, real_to_dolar_float)
main()