numeros = [10, 20, 30, 40]

def aumentar_numeros(numeros):

    return [numero*1.1 for numero in numeros]

resultado = aumentar_numeros(numeros)
print(resultado)