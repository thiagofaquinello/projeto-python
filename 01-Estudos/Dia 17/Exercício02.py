produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"]==nome:
            return produto
    return None



nome = input("Digite o produto: ")

resultado = buscar_produto(produtos, nome)

if resultado is not None:
    print("Produto encontrado:", resultado)
else:
    print("Produto não encontrado.")