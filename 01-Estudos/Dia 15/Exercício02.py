produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def buscar_produto(produtos, nome):
    for produto in produtos:
        if nome == produto["nome"]:
            return produto
        
    return None

nome = input("Digite o produto a ser procurado: ")
produto = buscar_produto(produtos, nome)

produto = buscar_produto(produtos, nome)

if produto is not None:
    print(produto)
else:
    print("Produto não encontrado.")