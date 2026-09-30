#dados = [1500, 10]
dados = (3200, 2)
def calcular_valor(preco, estoque):
    return preco * estoque

resultado = calcular_valor(*dados)
print(resultado)

