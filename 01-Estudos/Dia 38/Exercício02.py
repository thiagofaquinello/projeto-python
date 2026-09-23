produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 0},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]

def valor_total_com_estoque(produtos):

    return [produto["preco"]*produto["estoque"] for produto in produtos if produto["estoque"]>0]

resultado = valor_total_com_estoque(produtos)
print(resultado)