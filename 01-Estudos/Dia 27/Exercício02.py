produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def filtrar_produtos(produtos, condicao):

    resultado = []

    for produto in produtos:
        if condicao(produto):
            resultado.append(produto)
    
    return resultado

def condicao1(produto):
    if produto["estoque"]<5:
        return True
    return False

def condicao2(produto):
        if produto["preco"]>1000:
           return True
        return False

resultado1 = filtrar_produtos(produtos, condicao1)
resultado2 = filtrar_produtos(produtos, condicao2)

print(resultado1)
print(resultado2)