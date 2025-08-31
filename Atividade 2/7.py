
#7. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# A quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
import os

os.system ('clear')

total_km = float (input ('Informe a quantidade de km percorridos:'))
dias_utilizados = int (input('Há quantos dias o carro está alugado?'))
diária_carro = 60.00
km = 0.15

preço_total = ((dias_utilizados * diária_carro) + total_km * km)

print (f'Valor total da alocação: R$ {preço_total:.2f}')