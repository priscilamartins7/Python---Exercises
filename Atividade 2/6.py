#6. Implemente um programa para ler o preço do litro do combustível de um carro,
#ler o desempenho do veículo (km/l) e a distância entre duas cidades (km), e informar quantos litros
#e quanto dinheiro vai ser gasto para fazer uma viagem entre as duas cidades.
import os

os.system ('clear')
preço_combustível = float (input('Informe o preço do litro do combustível: R$'))
consumo_combustível = float (input ('Informe o consumo de combústivel por km/l: '))
distancia = float (input('Informe a distância percorrida entre as duas cidades: '))

litros_gasto = distancia / consumo_combustível
valor_gasto = litros_gasto *preço_combustível

print (f'Foram gastos {litros_gasto:.2f} litros e R$ {valor_gasto:.2f} para percorrer {distancia} km entre as duas cidades.')



