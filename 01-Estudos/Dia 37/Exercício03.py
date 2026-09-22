produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def calcular_valores_estoque(produtos_caros):

    return [produto["preco"]*produto["estoque"] for produto in produtos_caros]

def filtrar_produtos_caros(produtos, limite):

    return[produto for produto in produtos if produto["preco"]>limite]

produtos_caros = filtrar_produtos_caros(produtos, 1000)
resultado = calcular_valores_estoque(produtos_caros)
print(resultado)