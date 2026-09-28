numeros = [4, 7, 2, 9, 5]

def soma_grandes(numeros):
    soma = 0
    for numero in numeros:
        if numero>5:
            soma +=numero
    return soma
    
resultado = soma_grandes(numeros)
print(resultado)