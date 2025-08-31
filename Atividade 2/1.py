#1. Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.
import os

os.system ('clear')

valor_1 = int(input('DIGITE O PRIMEIRO VALOR:'))
valor_2 = int(input('DIGITE O SEGUNDO VALOR:'))

soma = valor_1 + valor_2
print (f'A soma entre os valores é: {soma}')