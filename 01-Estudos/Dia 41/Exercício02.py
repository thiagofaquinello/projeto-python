produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 1},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def menor_produto(produtos):

    if produtos:
        menor = produtos[0]["estoque"]
        for produto in produtos:
            if produto["estoque"]<menor:
                menor=produto["estoque"]
                menor_nome = produto["nome"]
        return menor_nome
    return None

resultado = menor_produto(produtos)
print(resultado)