def calcular_media(*numeros):

    if numeros:
        soma = 0
        contador = 0
        for numero in numeros:
            soma += numero
            contador += 1
        media = soma/contador
        return media
    return None

resultado = calcular_media(10,20,30)
print(resultado)