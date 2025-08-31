#2. Fazer um programa para receber 3 
# valores inteiros do usuário e mostrar a sua média.
import os

os.system ('clear')
valor_1 = int(input('DIGITE O PRIMEIRO VALOR:'))
valor_2 = int(input('DIGITE O SEGUNDO VALOR:'))
valor_3 = int(input('DIGITE O TERCEIRO VALOR:'))

média = (valor_1 + valor_2  + valor_3)/3
print (f'A média entre os valores é: {média}')