numeros = [2, 5, 8, 11, 14]

quadrado = lambda numero: numero*numero

resultado = map(quadrado, numeros)

print(list(resultado))