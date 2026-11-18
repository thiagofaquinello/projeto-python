sensores = {
    "A": {
        "temperatura": 72.0,
        "local": "Sala 1",
        "ativo": True
    },
    "B": {
        "temperatura": 88.5,
        "local": "Sala 2",
        "ativo": True
    },
    "C": {
        "temperatura": 65.0,
        "local": "Sala 3",
        "ativo": False
    }
}

novas_leituras = {
    "A": {
        "temperatura": 78.0,
        "ativo": True
    },
    "B": {
        "temperatura": 91.0,
        "ativo": False
    },
    "D": {
        "temperatura": 70.0,
        "ativo": True
    }
}

def atualizar_sensores(sensores, novas_leituras):

    for id_nova_leitura, dados_nova_leitura in novas_leituras.items():
            if id_nova_leitura in sensores:
                sensores[id_nova_leitura]["temperatura"] = dados_nova_leitura["temperatura"]
                sensores[id_nova_leitura]["ativo"] = dados_nova_leitura["ativo"]
            else:
                sensores[id_nova_leitura] = {
                "temperatura": dados_nova_leitura["temperatura"],
                "local": "Não definida",
                "ativo": dados_nova_leitura["ativo"],
                }
   
    return sensores

resultado = atualizar_sensores(sensores, novas_leituras)

assert resultado["A"]["temperatura"] == 78.0
assert resultado["A"]["local"] == "Sala 1"

assert resultado["B"]["temperatura"] == 91.0
assert resultado["B"]["ativo"] == False
assert resultado["B"]["local"] == "Sala 2"

assert resultado["C"]["temperatura"] == 65.0

assert resultado["D"]["temperatura"] == 70.0
assert resultado["D"]["local"] == "Não definida"

print(resultado)