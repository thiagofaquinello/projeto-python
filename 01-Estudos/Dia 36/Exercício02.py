produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def obter_precos_estoque_baixo(produtos):

    return[produto["preco"]*produto["estoque"] for produto in produtos if produto["estoque"]<5]

resultado = obter_precos_estoque_baixo(produtos)
print(resultado)