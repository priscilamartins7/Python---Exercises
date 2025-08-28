valor_kg = float (input('Informe o valor do kg:'))
pedido = float (input('Informe a quantidade comprada:'))
preço = valor_kg * pedido

print (f'Total a pagar: R$ {preço:.2f}')