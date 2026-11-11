sensores = {
    "A": 72.0,
    "B": 88.5,
    "C": 65.0,
    "D": 95.0,
    "E": 40.0
}

def analisar_sensores(sensores):

    acima_limite = []
    maior = sensores["A"]
    nome = "A"
    soma = 0
    for chave, sensor in sensores.items():
        if sensor > 80:
            acima_limite.append(chave)
        if maior<sensor:
            maior = sensor
            nome = chave
        soma += sensor
    media=soma/len(sensores)

    return {"quantidade": len(sensores),
    "acima_limite": acima_limite,
    "maior_sensor": nome,
    "maior_temperatura": maior,
    "temperatura_media": media
    }

resultado = analisar_sensores(sensores)
print(resultado)

assert resultado["quantidade"] == 5
assert resultado["maior_sensor"] == "D"
assert resultado["maior_temperatura"] == 95.0
assert resultado["temperatura_media"] == 72.1
assert "D" in resultado["acima_limite"]
assert "B" in resultado["acima_limite"]
assert "A" not in resultado["acima_limite"]