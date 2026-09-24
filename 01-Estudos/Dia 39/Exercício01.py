produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]

def acima_limite(produtos,limite):
    return [produto["nome"] for produto in produtos if produto["preco"]*produto["estoque"]>limite]
resultado = acima_limite(produtos, 7000)

print(resultado)