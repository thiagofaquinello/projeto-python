produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def calcular_valor_produto(produto):
    return produto["preco"] * produto["estoque"]

def encontrar_produto_mais_valioso(produtos):

    maior_valor = 0
    for produto in produtos:
        valor = calcular_valor_produto(produto)
        if valor>maior_valor:
            maior_valor=valor
            maior_produto=produto
    return maior_produto

resultado = encontrar_produto_mais_valioso(produtos)
print(resultado)

