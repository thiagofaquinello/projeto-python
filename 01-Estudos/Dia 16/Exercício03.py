produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 4}
]

def aplicar_desconto_produtos(produtos, percentual):
    for produto in produtos:
        produto["preco"] = produto["preco"]*((100-percentual)/100)
    return produtos

percentual = float(input("Digite o percentual de redução: "))
resultado = aplicar_desconto_produtos(produtos, percentual)
print(resultado)