#8. Escreva um programa para ler um uma temperatura em graus Fahrenheit
#calcular e escrever o valor correspondente em graus Celsius:
#C = ((F – 32)/9)*5

import os

os.system ('clear')

fahrenheit = float (input ('Informe a temperatura em graus Fahrenheit: '))
celsius = float ((fahrenheit - 32)/9)*5

print (f'RESULTADO:\nO valor que corresponde a celsius é igual a {celsius:.2f}°C.')