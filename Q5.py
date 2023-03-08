
frase = input("Digite uma string: ")

tam = len(frase)
letras = []

for i in range (tam):
    letras.append(frase[i])

i = 0
j = (tam - 1)

while (i < j):
    aux = letras[i]
    letras[i] = letras[j]
    letras [j] = aux
    i += 1
    j -= 1

for i in range (tam):
    print(letras[i], end="")




