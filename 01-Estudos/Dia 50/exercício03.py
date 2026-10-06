leituras = [
    {"sensor": "A", "valor": 72, "limite": 80},
    {"sensor": "B", "valor": 91, "limite": 85},
    {"sensor": "C", "valor": 68, "limite": 70},
    {"sensor": "D", "valor": 103, "limite": 90},
    {"sensor": "E", "valor": 77, "limite": 75},
]

def acima_limites(leituras):
    resumo_leituras = []
    for leitura in leituras:
        if leitura["valor"]>leitura["limite"]:
            excesso = leitura["valor"]-leitura["limite"]
            resumo_leituras.append({"sensor": leitura["sensor"], "valor": leitura["valor"], "excesso": excesso})
    return resumo_leituras
ordem_excessos = sorted(acima_limites(leituras), key = lambda leitura: leitura["excesso"], reverse=True)
print(ordem_excessos)