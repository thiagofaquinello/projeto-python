produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2100, "estoque": 5}
]

def verificar_estoque(produtos):
    produtos_com_estoque_baixo = []
    produtos_com_estoque_normal = []
    for produto in produtos:
        if produto["estoque"] >= 5:
            produtos_com_estoque_normal.append(produto["nome"])
        else:
            produtos_com_estoque_baixo.append(produto["nome"])
    return produtos_com_estoque_normal, produtos_com_estoque_baixo

produtos_com_estoque_normal, produtos_com_estoque_baixo = verificar_estoque(produtos)

print("Produtos com estoque baixo: ",produtos_com_estoque_baixo)
print("Produtos com estoque normal: ",produtos_com_estoque_normal)