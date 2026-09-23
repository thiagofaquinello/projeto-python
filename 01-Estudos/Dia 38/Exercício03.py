produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Inversor", "preco": 2200, "estoque": 4},
    {"nome": "Cabo", "preco": 80, "estoque": 20}
]

def produtos_de_alto_valor(produto):

    return produto["preco"]*produto["estoque"]>5000

def produtos_reposicao(produto):

    return produto["estoque"]<5

def obter_nomes(produtos, condicao):

    return [produto["nome"] for produto in produtos if condicao(produto)]

def valor_total(produtos):

    soma = 0
    for produto in produtos:
        soma += produto["preco"]*produto["estoque"]
    return soma

resultado1 = obter_nomes(produtos, produtos_de_alto_valor)
resultado2 = obter_nomes(produtos, produtos_reposicao)
resultado3 = valor_total(produtos)
print(f"Alto valor: {resultado1}\nPrecisam de reposição: {resultado2}\nValor total: {resultado3}")

