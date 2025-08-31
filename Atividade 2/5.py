#5. Implemente um programa para ler o salário mensal atual de um funcionário 
#e o percentual de reajuste. 
#Calcular e escrever o valor do novo salário.

import os

os.system ('clear')

salário = float (input('Por favor, informe o salário: R$'))
reajuste = float (input ('Por favor, informe o percentual (%) de reajuste: '))
percentual = ((reajuste/100)*salário) + salário
print (f'Salário com reajuste: R$ {percentual:.0f}.')