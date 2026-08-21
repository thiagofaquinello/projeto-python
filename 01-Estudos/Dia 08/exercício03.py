entradas = [1,2,3,4,5,6]

def separar_numeros(entradas):
    pares = []
    impares = []
    for entrada in entradas:
        if entrada%2 == 0:
            pares.append(entrada)
        else:
            impares.append(entrada)
    return pares, impares

pares, impares = separar_numeros(entradas)
print("Pares:", pares)
print("Ímpares:", impares)
