numeros = [4, 9, 12, 17, 20, 25]

def dobro_grandes(numeros):
    return [numero*2 for numero in numeros if numero>10]

resultado = dobro_grandes(numeros)
print(resultado)