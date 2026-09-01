produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def encontrar_produto(produtos, nome):

    for produto in produtos:
        if produto["nome"] == nome:
            return produto
    return None

def verificar_produto(produto):

    if produto["estoque"]<5:
        return "Estoque baixo"
    return "Estoque normal"

nome = input("Digite o produto desejado: ")
produto = encontrar_produto(produtos, nome)
if produto is not None:
    estoque = verificar_produto(produto)
    print(estoque)
else: 
    print("Produto não está presente na lista.")




