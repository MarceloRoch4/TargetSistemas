import json

with open("dados.json", encoding='utf-8') as data_JSON:
    dados = json.load(data_JSON)

valor_diario = []
dia_lista = []
fat_dia_superior = []
maior = 0
dias_0 = 0

for i in dados:
    valor_diario.append(i['valor'])
    dia_lista.append(i['dia'])


for j in range(len(valor_diario)-1):
    for i in range(len(valor_diario)-1):
        if int(valor_diario[i]) > int(valor_diario[i+1]):
            valor_diario[i], valor_diario[i+1] = valor_diario[i+1], valor_diario[i]
            dia_lista[i], dia_lista[i+1] = dia_lista[i+1], dia_lista[i]

for i in range(len(valor_diario)-1):
    if int(valor_diario[i]) == 0:
        dias_0 += 1

print(f"O menor valor de faturamento ocorrido em um dia do mês:  R$ {valor_diario[dias_0]:.2f} no dia {dia_lista[dias_0]}")
print("---------------------------------------------------------------------------")

print(f"O maior valor de faturamento ocorrido em um dia do mês:  R$ {valor_diario[-1]:.2f} no dia {dia_lista[-1]}")



#Descobrir média
soma = 0

for i in dados:
    soma += i['valor']


dias_cont = len(valor_diario) - dias_0
media = soma/dias_cont
print("---------------------------------------------------------------------------")

print(f"Os dias contabilizados são: {dias_cont}")
print("---------------------------------------------------------------------------")
print(f"A média dos valores mensais é: R$ {media:.2f}")

#Número de dias no mês em que o valor do faturamento diário foi superior à media mensal

for i in range(len(valor_diario)):
    if int(valor_diario[i]) > media:
        fat_dia_superior.append(dia_lista[i])
        
print("---------------------------------------------------------------------------")

fat_dia_superior.sort() #ordernar os números
print(f"São {len(fat_dia_superior)} o número de dias que o valor de faturamento diário foi superior à media mensal, sendo os dias {fat_dia_superior}")

print("---------------------------------------------------------------------------")



    