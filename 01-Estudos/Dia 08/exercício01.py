numeros = [4, 7, 2, 9, 10, 3]

soma = 0
valor = 0
par = 0
impar = 0
for numero in numeros:
    soma+=numero
    if numero >= valor:
        valor = numero
    if numero%2 == 0:
        par += 1
    else:
        impar += 1
print("Soma da lista = ",soma)
print("Maior número é: ",valor)
print("A quantidade de números pares é: ",par)
print("A quantidade de números ímpares é: ",impar)