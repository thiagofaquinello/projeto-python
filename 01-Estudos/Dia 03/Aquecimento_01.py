numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in numeros:
    print(numero, end=" ")
print("\n")
for numero in numeros:
    if numero%2==0:
            print(numero, end=" ")
print("\n")
for numero in numeros:
    soma+=numero
print(soma)