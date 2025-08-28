import os
# CÓDIGO FEITO ANTES DA CORREÇÃO:
#número = int (input ('Insira um número (máx.3 algarismos):'))
#print (f'Centena: {número//100}')
#print (f'Dezena: {número%100//10}')
#print (f'Unidade: {número%100%10}')

#DICA: FORMA QUE CONSERVA AS VARIÁVEIS PARA SER USADAS PORSTERIORMENTE
número = int (input ('Insira um número (máx.3 algarismos):'))
centenas = número//100
dezenas = número%100//10
unidade = número%100%10
print (f'Centenas: {centenas}, dezenas: {dezenas} e {unidade} unidade.')