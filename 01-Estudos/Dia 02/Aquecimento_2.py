x = 0
lista = []
soma = 0
while x != -1:
    x = float(input("Para sair digite -1. Digite um número: "))

    if x != -1:
        lista.append(x)
for numero in lista:
    soma+=numero

media=soma/len(lista)
print(media)