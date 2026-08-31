produto = {
    "nome": "Motor",
    "preco": 1500,
    "estoque": 10
}

def verificar_estoque(produto):

    if produto["estoque"]<5:
        return "Estoque baixo"
    else :
        return "Estoque normal"

resultado = verificar_estoque(produto)
print(resultado)
