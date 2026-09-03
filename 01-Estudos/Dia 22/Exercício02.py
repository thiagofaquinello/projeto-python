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

def selecionar_produto(produtos):

    nome = input("Digite o nome do produto: ")
    return buscar_produto(produtos, nome)
    

resultado = selecionar_produto(produtos)
if resultado is not None:
    print(resultado)
else:
    print("Produto não localizado.")


