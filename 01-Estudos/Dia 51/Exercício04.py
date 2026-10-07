leituras = [
    {"sensor": "A", "valor": 72, "limite": 80},
    {"sensor": "B", "valor": 91, "limite": 85},
    {"sensor": "C", "valor": 68, "limite": 70},
    {"sensor": "D", "valor": 103, "limite": 90},
    {"sensor": "E", "valor": 77, "limite": 75},
]

def analisar_sensores(leituras):
    contador = 0
    for leitura in leituras:
        if leitura["valor"]>leitura["limite"]:
            contador += 1
    existe_falha = any(leitura["valor"]>leitura["limite"] for leitura in leituras)
    todos_abaixo_110 = all(leitura["valor"]<110 for leitura in leituras)
    return {"quantidade": len(leituras), "quantidade_acima_limite": contador, "existe_falha": existe_falha, "todos_abaixo_110": todos_abaixo_110}

resumo = analisar_sensores(leituras)
print(resumo)