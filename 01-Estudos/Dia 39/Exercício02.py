produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]

def maior_produto(produtos):

    maior_valor = 0
    for produto in produtos:
        if produto["preco"]*produto["estoque"]>maior_valor:
            maior_valor = produto["preco"]*produto["estoque"]
            maior = produto
    return maior

resultado = maior_produto(produtos)
print(resultado)