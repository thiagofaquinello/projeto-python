produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def filtrar_estoque_baixo(produtos):

    resultado = []

    for produto in produtos:
        if estoque_abaixo_do_limite(produto, 5):
            resultado.append(produto)
    
    return resultado

def estoque_abaixo_do_limite(produto, limite):

    if produto["estoque"]<limite:
        return True
    return False

resultado = filtrar_estoque_baixo(produtos)
print(resultado)

