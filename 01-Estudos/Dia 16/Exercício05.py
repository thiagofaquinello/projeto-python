produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def analisar_estoque(produtos):
    
    maior_valor = produtos[0]
    menor_valor = produtos[0]
    for produto in produtos:
        if produto["preco"]*produto["estoque"] > maior_valor["preco"]*maior_valor["estoque"]:
            maior_valor = produto
        if produto["preco"]*produto["estoque"] < menor_valor["preco"]*menor_valor["estoque"]:
            menor_valor = produto
    return maior_valor, menor_valor

maior_valor, menor_valor = analisar_estoque(produtos)
print(maior_valor)
print(menor_valor)