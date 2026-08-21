entradas = [1,2,3,4,5,6]
pares = []
impares = []

for entrada in entradas:
    if entrada%2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)

print(pares)
print(impares)