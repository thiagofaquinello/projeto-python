numeros = [10, 5, 38, 20, 3, 7]

def analisar_numeros(numeros):
    soma = 0
    maior_numero=numeros[0]
    for numero in numeros:
        soma += numero
        if numero>=maior_numero:
            maior_numero=numero
    media=soma/len(numeros)
    return soma, maior_numero, media

soma, maior_numero, media = analisar_numeros(numeros)
print("A soma dos números é: ",soma)
print("O maior dos números é: ", maior_numero)
print("A média dos números é: ", media)