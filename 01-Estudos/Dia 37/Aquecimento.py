numeros = [3, 6, 9, 12, 15]

def obter_pares(numeros):

    return [numero for numero in numeros if numero%2==0]

resultado = obter_pares(numeros)
print(resultado)