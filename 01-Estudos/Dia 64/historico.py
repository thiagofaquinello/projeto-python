historico = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5},
    {"sensor": "C", "temperatura": 65.0}
]

novas_leituras = [
    {"sensor": "B", "temperatura": 90.0},
    {"sensor": "D", "temperatura": 76.0},
    {"sensor": "E", "temperatura": "abc"},
    {"sensor": "A", "temperatura": 80.0}
]

from validacao import validar_temperatura

def atualizar_historico(historico_teste, leituras_teste):
    sensores = {}
    for leitura in historico_teste:
        sensores[leitura["sensor"]] = leitura["temperatura"]
    for nova_leitura in leituras_teste:
        resulta = validar_temperatura(nova_leitura.get("temperatura"))
        if resulta is not None:
            sensor = nova_leitura["sensor"]
            sensores[sensor] = resulta
    resultado = []
    for sensor, temperatura in sensores.items():
        resultado.append({
            "sensor": sensor,
            "temperatura": temperatura
        })
    return resultado

if __name__ == "__main__":
    resultado = atualizar_historico(historico, novas_leituras)
    print(resultado)
    assert len(resultado) == 4

    teste = {item["sensor"]: item["temperatura"] for item in resultado}

    assert teste["A"] == 80.0
    assert teste["B"] == 90.0
    assert teste["C"] == 65.0
    assert teste["D"] == 76.0
    assert "E" not in teste

