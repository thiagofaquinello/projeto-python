produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def produto_caro(produto, preco_minimo):
    
    if produto["preco"]>preco_minimo:
        return True
    return False
            

resultado = produto_caro(produtos[0], 1000)
#resultado = produto_caro(produtos[1], 1000)

if resultado:
    print("Produto é caro.")
else:
    print("Produto é barato.")
    