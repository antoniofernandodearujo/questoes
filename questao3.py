"""
    @author: Antonio Fernando
    data: 14/06/2022
"""

import json

with open("dados.json", encoding='utf-8') as meu_json:
	dados = json.load(meu_json)


soma = 0
#Contador responsável pela a quantidade de dias que o valor não é 0.
cont = 0
maior = menor = dados[0]['valor']
quantDiasMaiorQueMedia = 1
# para cada item do arquivo json
for i in dados:
    if i['valor'] > maior:
        maior = i['valor']
        
    if i['valor'] < menor:
        menor = i['valor']
        
    if i['valor'] > 0:
        soma += i['valor']
        cont += 1
        
    media = soma / cont
    
    if i['valor'] > media:
        quantDiasMaiorQueMedia += 1
    



print('O menor valor e {}'.format(menor))
print('O maior valor e {}'.format(maior))
print('{} dias do mes que foi maior que a media mensal({})'.format(quantDiasMaiorQueMedia, media))


