produto = {
    "nome": "Motor",
    "preco": 1500,
    "estoque": 10
}

def aumentar_estoque(produto, quantidade):
    produto["estoque"]=produto["estoque"]+quantidade
    return produto

resultado = aumentar_estoque(produto, 6)
print(resultado)