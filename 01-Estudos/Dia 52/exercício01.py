sensores = [
    {"nome": "S1", "valor": 42, "limite": 50},
    {"nome": "S2", "valor": 78, "limite": 70},
    {"nome": "S3", "valor": 65, "limite": 65},
    {"nome": "S4", "valor": 91, "limite": 80},
]
#sensores = []

acima_limite = lambda sensor: sensor["valor"]>sensor["limite"]

def relatorio(sensores):
    if sensores:
        estado_critico = []
        maior_valor = sensores[0]["valor"]
        nome_sensor = sensores[0]["nome"]
        for sensor in sensores:
            resultado1 = acima_limite(sensor)
            if resultado1:
                estado_critico.append(sensor)
            if sensor["valor"]>maior_valor:
                maior_valor=sensor["valor"]
                nome_sensor = sensor["nome"]
        return {"Quantidade_total": len(sensores), "Quantidade_acima_limite": len(estado_critico), "Sensor_com_maior_valor": nome_sensor, "Sensores_estado_critico": estado_critico}
    return {"Quantidade_total": len(sensores), "Quantidade_acima_limite": 0, "Sensor_com_maior_valor": None, "Sensores_estado_critico": []}

resumo = relatorio(sensores)
print(resumo)