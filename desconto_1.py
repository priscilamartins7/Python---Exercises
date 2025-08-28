# OPÇÃO 1
valor_produto = float(input('Informe o valor do produto: R$'))
desconto = 10
valor_desconto = float((valor_produto * desconto) / 100)
total = valor_produto - valor_desconto
print(f'Total a pagar com desconto: R$ {total:.2f}')

# OPÇÃO 2
valor_produto = float(input('Informe o valor do produto: R$'))
desconto = 10
valor_desconto = ((100 - desconto) / 100)*valor_produto
print(f'Total a pagar com desconto: R$ {valor_desconto:.2f}')