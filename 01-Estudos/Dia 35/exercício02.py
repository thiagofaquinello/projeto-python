produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def filtrar_produtos(produtos, condicao):
    return [produto["nome"] for produto in produtos if condicao(produto)]
def estoque_baixo(produto):
    return produto["estoque"]<5

resultado = filtrar_produtos(produtos, estoque_baixo)
print(resultado)