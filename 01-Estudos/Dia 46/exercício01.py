produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
]

def calcular_valor(preco, estoque, **kwargs):
    return preco*estoque
def analisar_produtos(produtos):
    lista = []
    for produto in produtos:
        calculo = calcular_valor(**produto)
        lista.append(calculo)
    return lista

resultado = analisar_produtos(produtos)
print(resultado)

