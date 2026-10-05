produtos = [
    {"nome": "Motor", "preco": 1500},
    {"nome": "Sensor", "preco": 250},
    {"nome": "CLP", "preco": 3200},
    {"nome": "Arduino", "preco": 180},
]

def filtrar_produtos(produtos, condicao):
    lista = []
    for produto in produtos:
        if condicao(produto):
            lista.append(produto)
    return lista
maiores = lambda produto: produto["preco"]>1000
menores = lambda produto: produto["preco"]<500
resultado1 = filtrar_produtos(produtos, maiores)
resultado2 = filtrar_produtos(produtos, menores)
print(resultado1)
print(resultado2)