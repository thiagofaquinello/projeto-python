produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def calcular_valor_produto(produto):
    return produto["preco"] * produto["estoque"]

def calcular_valor_estoque(produtos):
    total = 0

    for produto in produtos:
        total += calcular_valor_produto(produto)

    return total

valor_total = calcular_valor_estoque(produtos)

print(valor_total)