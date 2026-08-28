produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def produtos_caros(produtos):
    produtos_acima_de_1000 = []
    for produto in produtos:
        if produto["preco"]>1000:
            produtos_acima_de_1000.append(produto)
    return produtos_acima_de_1000

def estoque_baixo(produtos):
    produtos_com_estoque_baixo = []
    for produto in produtos:
        if produto["estoque"]<5:
            produtos_com_estoque_baixo.append(produto)
    return produtos_com_estoque_baixo

resultado1 = produtos_caros(produtos)
resultado2 = estoque_baixo(produtos)
print(resultado1)
print(resultado2)
