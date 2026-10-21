sensores = [
    {"sensor": "A", "valor": 72, "limite": 80},
    {"sensor": "B", "valor": 91, "limite": 85},
    {"sensor": "C", "valor": 68, "limite": 70},
    {"sensor": "D", "valor": 103, "limite": 90},
    {"sensor": "E", "valor": 77, "limite": 75},
]

def sensor_acima_limite(sensor):
    return sensor["valor"]>sensor["limite"]

acima_limites = [sensor for sensor in sensores if sensor_acima_limite(sensor)]

def relatorio(sensores, acima_limites):
    nome = [sensor["sensor"] for sensor in acima_limites]
    return {
    "total_sensores": len(sensores),
    "sensores_criticos": len(acima_limites),
    "nomes_criticos": nome
    }

resultado = relatorio(sensores, acima_limites)
print(resultado)