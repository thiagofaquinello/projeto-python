equipamentos = [
    {"nome": "Motor A", "potencia": 1500, "temperatura": 65},
    {"nome": "Motor B", "potencia": 2200, "temperatura": 82},
    {"nome": "Motor C", "potencia": 1100, "temperatura": 58},
    {"nome": "Motor D", "potencia": 3000, "temperatura": 91}
]

def equipamentos_criticos(equipamentos):
    equipamentos_críticos = []
    for equipamento in equipamentos:
        if equipamento["temperatura"] > 80 or equipamento["potencia"] > 2500:
            equipamentos_críticos.append(equipamento)
    return equipamentos_críticos

def temperatura_media(equipamentos):
    soma = 0
    for equipamento in equipamentos:
        soma += equipamento["temperatura"]
    media = soma/len(equipamentos)
    return media

equipamentos_críticos = equipamentos_criticos(equipamentos)
media = temperatura_media(equipamentos)

print("Equipamentos críticos: ",equipamentos_críticos)
print("Temperatura média:", media, "graus Celsius")