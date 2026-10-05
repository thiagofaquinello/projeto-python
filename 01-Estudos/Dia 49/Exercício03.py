produtos = [
    {"nome": "Motor", "preco": 1500},
    {"nome": "Sensor", "preco": 250},
    {"nome": "CLP", "preco": 3200},
]

def calcular_valor(produto):
    return produto["preco"]*2

resultado = list(map(calcular_valor,produtos))
print(resultado)