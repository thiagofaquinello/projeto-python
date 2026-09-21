produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def obter_precos(produtos):

    return [produto["preco"] for produto in produtos]

def aumentar_precos(produtos, percentual):

    produtos_precos = obter_precos(produtos)
    return [produto_preco*(1+percentual/100) for produto_preco in produtos_precos]

resultado = aumentar_precos(produtos, 10)
print(resultado)