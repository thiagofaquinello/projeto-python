numeros = [2, 5, 8, 11, 14, 17]

def analise_numero(numero):
    if numero>10:
        return True
    return False

resultado = filter(analise_numero, numeros)
resultado = list(resultado)
print(resultado)