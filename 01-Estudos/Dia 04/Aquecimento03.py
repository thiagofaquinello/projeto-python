numeros = [10,20,30,40,50]

def lista(numeros):
    soma = 0 
    for numero in numeros:
        soma += numero
    return soma

print(lista(numeros))