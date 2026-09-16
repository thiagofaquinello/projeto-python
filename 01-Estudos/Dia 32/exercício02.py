produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

produto_com_estoque_abaixo_do_limite = [produto["nome"] for produto in produtos if produto["estoque"]<5]

print(produto_com_estoque_abaixo_do_limite)