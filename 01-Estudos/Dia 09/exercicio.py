numeros = [12, 5, 8, 21, 1, 17, 10]

def analisar_numeros(numeros):
    valor_max = 0
    valor_min = numeros[0]
    par = 0
    impar = 0
    for numero in numeros:
        if numero >= valor_max:
            valor_max = numero
        if numero <= valor_min:
            valor_min = numero    
        if numero%2 == 0:
            par += 1
        else:
            impar += 1
    return valor_max, valor_min, par, impar

valor_max, valor_min, par, impar = analisar_numeros(numeros)
print("O maior valor é: ", valor_max)
print("O menor valor é: ", valor_min)
print("A quantidade de pares é: ", par)
print("A quantidade de ímpares é: ", impar)


