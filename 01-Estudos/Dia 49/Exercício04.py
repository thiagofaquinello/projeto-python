produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
]

def gerar_resumo(produto):
    return {"nome": produto["nome"], "valor_estoque": produto["preco"]*produto["estoque"]}

resultado = list(map(gerar_resumo, produtos))
print(resultado)