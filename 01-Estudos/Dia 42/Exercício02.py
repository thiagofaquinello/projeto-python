produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]
#produtos = []

def analise(produtos):
    soma1 = 0
    soma2 = 0
    soma3 = 0
    for produto in produtos:
        soma1 += 1
        preco = produto["estoque"]*produto["preco"]
        soma2 +=preco
        soma3 += produto["estoque"]
    return {"quantidade_produtos": soma1,"valor_total": soma2,"estoque_total": soma3}

resultado = analise(produtos)
print(resultado)