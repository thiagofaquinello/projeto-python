numeros = [10, 5, 8, 20, 3, 7]

def analisar_lista(numeros):
    soma = 0
    maior_numero=numeros[0]
    menor_numero=numeros[0]
    i=0
    f=0
    for numero in numeros:
        soma += numero
        if numero>=maior_numero:
            maior_numero=numero
        if numero<=menor_numero:
            menor_numero=numero
        if numero%2==0:
            i+=1
        else:
            f+=1
    media=soma/len(numeros)
    return maior_numero, menor_numero, media, i, f

maior_numero, menor_numero, media, i, f = analisar_lista(numeros)
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
print(f"A média dos números é: {media}")
print(f"A quantidade de pares é: {i}")
print(f"A quantidade de impares é: {f}")

