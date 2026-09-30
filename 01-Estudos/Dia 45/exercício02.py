produto = {
    "nome": "Arduino",
    "preco": 180,
    "estoque": 8
}

def criar_produto(nome, preco, estoque):
    return {
        "nome": nome,
        "valor_estoque": preco * estoque
    }

resultado = criar_produto(**produto)
print(resultado)