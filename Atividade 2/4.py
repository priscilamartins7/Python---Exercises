#4. Escreva um programa que armazene um valor de entrada em uma variável A e outro em uma variável B. 
#A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo
#com que o valor que está em A passe para B e vice-versa. 
#Ao final escrever os valores que ficaram armazenados nas variáveis.

import os

os.system ('clear')

A = int (input ('Valor de A:'))
B = int (input ('Valor de B:'))
armazenamento = A
A = B
B = armazenamento
print (f'Valor de A: {A} \nValor de B: {B}')