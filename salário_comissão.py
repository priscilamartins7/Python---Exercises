# opção 1
salário = float (input('Informe o salário:'))
vendas = float (input ('Informe as vendas:'))
comissão = 4*vendas
salário_fixo = salário + comissão 

print(f'Valor do salário fixo: R$ {salário_fixo:.2f}')

# opção 2
salário_fixo2 = ((4/100)*vendas) + salário
print(f'Valor do salário fixo: R$ {salário_fixo:.2f}')