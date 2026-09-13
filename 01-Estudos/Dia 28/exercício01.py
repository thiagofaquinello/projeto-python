produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def verificar_preco(produto,limite):

    if produto["preco"] > limite:
        return True
    return False

def verificar_estoque(produto,limite):

    if produto["estoque"] < limite:
        return True
    return False

def filtrar_produtos(produtos, funcao,limite):

    resultado = []

    for produto in produtos:
        if funcao(produto,limite):
            resultado.append(produto)
    
    return resultado

resultado1 = filtrar_produtos(produtos, verificar_preco,200)
resultado2 = filtrar_produtos(produtos, verificar_estoque,8)

print(resultado1)
print(resultado2)
