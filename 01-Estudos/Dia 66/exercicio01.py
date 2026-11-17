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

resultado = analisar_sensores(sensores)
print(resultado)
        
