produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def calcular_valor_total(produtos):

    valor_total = 0
    for produto in produtos:
        valor_total += produto["preco"]*produto["estoque"]
    return valor_total

resultado = calcular_valor_total(produtos)
print("O valor total é de R$", resultado)