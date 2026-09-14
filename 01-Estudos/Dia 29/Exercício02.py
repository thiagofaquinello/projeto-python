produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

verificar_preco_e_estoque = lambda produto, limite1, limite2: produto["preco"]>limite1 and  produto["estoque"] < limite2

def filtrar_produtos(produtos, funcao,limite1, limite2):

    resultado = []

    for produto in produtos:
        if funcao(produto,limite1, limite2):
            resultado.append(produto)
    
    return resultado

resultado = filtrar_produtos(produtos, verificar_preco_e_estoque,500,10)
print(resultado)