produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]
def filtrar_estoque_baixo(produtos, limite):

    return [produto for produto in produtos if produto["estoque"]<limite]

def calcular_valor_estoque(produtos_estoque_limite):

    return [produto["preco"]*produto["estoque"] for produto in produtos_estoque_limite]

def obter_nomes(produtos_estoque_limite):

    return [produto["nome"] for produto in produtos_estoque_limite]


produtos_estoque_limite = filtrar_estoque_baixo(produtos, 5)
resultado1 = obter_nomes(produtos_estoque_limite)
resultado2 = calcular_valor_estoque(produtos_estoque_limite)
print(f"Nomes: {resultado1}\nValores: {resultado2}")