def criar_produto(**dados):
    return dados

produto = criar_produto(
    nome="Arduino",
    preco=180,
    estoque=8,
    categoria="Eletronica"
)

print(produto)