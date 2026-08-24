produto = {
    "nome": "Motor",
    "preco": 1500,
    "estoque": 3
}

def atualizar_preco(produto):
    print("Preço atual do produto é R$", produto["preco"])
    novo_preco = float(input("Digite o novo preço do produto: "))
    produto["preco"]= novo_preco
    return produto

print(atualizar_preco(produto))