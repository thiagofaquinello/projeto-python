produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def calcular_valor_estoque(produtos):
    valor_total = 0
    for produto in produtos:
        valor = produto["preco"]*produto["estoque"]
        valor_total += valor
        

    return valor_total

resultado = calcular_valor_estoque(produtos)
print(f"O valor total do estoque é: {resultado}")