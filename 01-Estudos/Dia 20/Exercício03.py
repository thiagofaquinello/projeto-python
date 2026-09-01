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

def atualizar_preco(produto, novo_preco):

    if novo_preco >= 0:
        produto["preco"] = novo_preco
        return produto
    return None

nome = input("Digite o produto desejado: ")
produto = encontrar_produto(produtos, nome)
if produto is not None:
    novo_preco = float(input("Digite o novo preço: "))
    novo_valor = atualizar_preco(produto, novo_preco)
    if novo_valor is not None:
        print("Produto atualizado: ", novo_valor)
    else:
        print("Preço inválido.")
else: 
    print("Produto não está presente na lista.")