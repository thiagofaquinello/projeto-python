produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
]
def processar_produtos(produtos):
    contador = 0
    soma = 0
    maior = 0
    
    for produto in produtos:
        contador+=1
        valor = calcular_valor(**produto)
        soma += valor
        if valor>maior:
            maior = valor
            maior_nome=produto["nome"]
    return {"Quantidade": contador, "valor_total": soma, "produto_maior_valor": maior_nome}
def calcular_valor(preco,estoque, **kwargs):
    return preco*estoque
resultado = processar_produtos(produtos)
print(resultado)