produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "CLP", "preco": 3200, "estoque": 2},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
]

filtro = [produto for produto in produtos if produto["estoque"]<5]
organizar = sorted(filtro, key = lambda produto: produto["preco"], reverse=True)
final = [produto["nome"] for produto in organizar]

print(final)