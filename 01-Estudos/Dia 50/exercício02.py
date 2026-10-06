produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
]

filtro_por_estoque = [produto for produto in produtos if produto["estoque"]<5]
def calculo_valor_total(filtro_por_estoque):
    lista_produtos = []
    for produto in filtro_por_estoque:
        valor = produto["preco"]*produto["estoque"]
        lista_produtos.append({"nome": produto["nome"], "valor_estoque": valor})
    return lista_produtos

organizar = sorted(calculo_valor_total(filtro_por_estoque), key = lambda produto: produto["valor_estoque"], reverse=True)

print(organizar)