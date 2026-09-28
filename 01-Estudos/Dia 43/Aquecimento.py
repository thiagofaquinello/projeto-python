def somar(*numeros):
    soma  = 0 
    for numero in numeros:
        soma += numero
    return soma

resultado = somar(10,20,30)
print(resultado)