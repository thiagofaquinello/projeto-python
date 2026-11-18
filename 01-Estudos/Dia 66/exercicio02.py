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
    },
    "D": {
        "temperatura": 95.0,
        "local": "Sala 4",
        "ativo": True
    }
}

novas_leituras = {
    "A": {
        "temperatura": 78.0,
        "ativo": True
    },
    "B": {
        "temperatura": 91.0,
        "ativo": True
    },
    "E": {
        "temperatura": 70.0,
        "ativo": True
    }
}
def analisar_sensores(sensores):
    contador1 = 0
    contador2 = 0
    contador3 = 0
    acima_limite = []
    soma = 0
    for id_sensores, dados in sensores.items(): 
        contador1 += 1
        if dados["ativo"]:
            contador2 += 1
            if dados["temperatura"]>80:
                acima_limite.append(id_sensores)
            soma += dados["temperatura"]
        
            
    media = soma/contador2
    quantidade_inativos= contador1-contador2
    return {
    "total":contador1,
    "ativos": contador2,
    "inativos": quantidade_inativos,
    "acima_limite": acima_limite,
    "media_ativos": media
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

resultado = analisar_sensores(sensores)

assert resultado["total"] == 4
assert resultado["ativos"] == 3
assert resultado["inativos"] == 1
assert resultado["acima_limite"] == ["B", "D"]

atualizado = atualizar_sensores(sensores, novas_leituras)

assert atualizado["A"]["temperatura"] == 78.0
assert atualizado["B"]["temperatura"] == 91.0
assert atualizado["E"]["local"] == "Não definida"
assert atualizado["C"]["temperatura"] == 65.0