numeros = [10, 20, 30, 40, 50]

def filtrar_maiores(numeros, limite):
    numeros_acima_do_limite = []
    for numero in numeros:
        if numero > limite:
            numeros_acima_do_limite.append(numero)
    return numeros_acima_do_limite
resultado = filtrar_maiores(numeros, 25)
print(resultado)