produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def filtrar_produtos_caros(produtos, limite):

    return[produto for produto in produtos if produto["preco"]>limite]

resultado = filtrar_produtos_caros(produtos, 1000)
print(resultado)