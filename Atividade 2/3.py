#3. Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
import os

os.system ('clear')

metros = int (input('DIGITE O VALOR EM METRO(S): '))
milímetros = metros * 1000

print ()

print (f'{metros} METRO(S) EQUIVALE(M) A {milímetros} MILÍMETRO(S).')
print ()