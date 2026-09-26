produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4}
]

def calcular_valor_produto(produto):
    
    return produto["preco"]*produto["estoque"]
    
def maior_produto(produtos):
    if produtos:
        maior_valor = 0
        for produto in produtos:
            valor = calcular_valor_produto(produto)
            if valor>maior_valor:
                maior_valor = valor
                maior = produto
        return maior
    return None

resultado = maior_produto(produtos)
print(resultado)