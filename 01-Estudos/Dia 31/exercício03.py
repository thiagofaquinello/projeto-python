produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

limite_estoque = lambda produto: produto["estoque"]<5
resultado1 = list(filter(limite_estoque, produtos))

nome_produtos_estoque_baixo = lambda produto: produto["nome"]
resultado2 = map(nome_produtos_estoque_baixo, resultado1)

print(list(resultado2))