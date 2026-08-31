produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def produtos_estoque_baixo(produtos, limite):

    estoque_abaixo_do_limite = []
    for produto in produtos:
        if produto["estoque"]< limite:
            estoque_abaixo_do_limite.append(produto)
    return estoque_abaixo_do_limite

resultado = produtos_estoque_baixo(produtos, 5)
print(resultado)