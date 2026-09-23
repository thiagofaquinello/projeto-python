numeros = [12, 5, 8, 21, 30, 7, 16]

def maiores_que_10(numeros):

    return [numero for numero in numeros if numero>10]

resultado = maiores_que_10(numeros)
print(resultado)