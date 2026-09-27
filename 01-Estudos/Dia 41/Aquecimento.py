#numeros = [8, 15, 3, 27, 11]
numeros = []
def maior_numero(numeros):
    if numeros:
        maior = 0
        for numero in numeros:
            if numero>maior:
                maior = numero
        return maior
    return None

resultado = maior_numero(numeros)
print(resultado)