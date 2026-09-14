produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

verificar_produto = lambda produto:  produto["preco"]>500 and produto["estoque"]<10

resultado = list(filter(verificar_produto, produtos))
print(resultado)