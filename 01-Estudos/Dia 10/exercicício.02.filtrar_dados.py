produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2100, "estoque": 5}
]

def produtos_caros(produtos):
    produtos_acima_de_1000 = []
    for produto in produtos:
        if produto["preco"] > 1000:
            produtos_acima_de_1000.append(produto["nome"])
    return produtos_acima_de_1000

print("Produtos acima de R$ 1000: ",produtos_caros(produtos))