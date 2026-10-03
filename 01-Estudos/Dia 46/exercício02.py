produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
]

def resumir_produto(nome, preco, estoque):
    return {
    "nome": nome,
    "valor_estoque": preco*estoque,
    "estoque_baixo": estoque<5
}
def analisar_produtos(produtos):
    lista = []
    for produto in produtos:
        resumo = resumir_produto(**produto)
        lista.append(resumo)
    return lista

resultado = analisar_produtos(produtos)
print(resultado)