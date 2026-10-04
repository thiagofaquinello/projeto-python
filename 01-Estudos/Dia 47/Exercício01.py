equipamentos = [
    {"nome": "Motor A", "temperatura": 72, "limite": 80},
    {"nome": "Motor B", "temperatura": 91, "limite": 85},
    {"nome": "Motor C", "temperatura": 68, "limite": 70},
]

def verificar_temperatura(nome, temperatura, limite):
    return {"nome": nome,
    "temperatura": temperatura,
    "acima_limite": temperatura>limite}
def analisar_equipamentos(equipamentos):
    lista = []
    for equipamento in equipamentos:
        equipamentos_afetados = verificar_temperatura(**equipamento)
        if equipamentos_afetados["acima_limite"]:
            lista.append(equipamentos_afetados)
    return lista
resultado = analisar_equipamentos(equipamentos)
print(resultado)
