equipamentos = [
    {"nome": "Motor A", "potencia": 1500, "horas": 8},
    {"nome": "Motor B", "potencia": 2200, "horas": 6},
    {"nome": "Bomba A", "potencia": 1000, "horas": 10},
    {"nome": "Compressor", "potencia": 3000, "horas": 4}
]

def calcular_consumo(equipamentos):
    consumo_alto = []
    for equipamento in equipamentos:
        consumo = equipamento["potencia"]*equipamento["horas"]
        if consumo > 10000:
            consumo_alto.append(equipamento)
    return consumo_alto

resultado = calcular_consumo(equipamentos)
print(resultado)