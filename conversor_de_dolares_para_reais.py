
import requests

reques = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

json = reques.json()

real = json['USDBRL']['high']

name = json['USDBRL']['name']

print('Programa para conversão de {0}'.format(name))

dol = float(input('Insira o valor em dolar a ser convertido:'))

print('O resultado da conversão foi:R${:.2f}'.format(dol * float(real)))