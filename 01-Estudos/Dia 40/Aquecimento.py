#numeros = [10,20,30]
numeros = []
def calcular_media(numeros):
    soma = 0
    if numeros != []:
        for numero in numeros:
            soma += numero
        media = soma/len(numeros)
        return media
    return None

resultado = calcular_media(numeros)
print(resultado)