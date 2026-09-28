produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]

def soma_valor_estoque_baixo(produtos):

    soma = 0
    for produto in produtos:
        if produto["estoque"]<5:
            preco = produto["estoque"]*produto["preco"]
            soma +=preco
    return soma

resultado = soma_valor_estoque_baixo(produtos)
print(resultado)