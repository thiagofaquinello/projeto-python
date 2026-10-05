precos = [100, 250, 500, 1000]
resultado = list(map(lambda preco: (preco-preco*0.1), precos))
print(resultado)