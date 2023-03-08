import json

with open("faturamento_Q4.json", encoding='utf-8') as data_JSON:
    dados = json.load(data_JSON)

soma = 0

for i in dados:
    soma += i['valor']
print("---------------------------------------------------------------------------")
print(f"A soma total é R$ {soma:.2f}, que representa 100% do faturamento.")
print("---------------------------------------------------------------------------")
for i in dados:
    percentual = (100*i['valor']/soma)
    print(f"{i['estado']} representa um percentual de {percentual:.2f}% dentro do valor total mensal da distribuidora." )
print("---------------------------------------------------------------------------")
