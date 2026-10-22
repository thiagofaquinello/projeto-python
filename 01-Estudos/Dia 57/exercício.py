historico = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5},
    {"sensor": "C", "temperatura": 65.0}
]

novas_leituras = [
    {"sensor": "B", "temperatura": 90.0},
    {"sensor": "D", "temperatura": 76.0}
]

def atualizar_historico(historico, novas_leituras):

    for nova_leitura in novas_leituras:
        encontrado = False
        for leitura in historico:
            if leitura["sensor"]==nova_leitura["sensor"]:
                leitura["temperatura"]=nova_leitura["temperatura"]
                encontrado = True
                break
        if not encontrado:
            historico.append(nova_leitura)
    
    return historico

resultado = atualizar_historico(historico, novas_leituras)
print(resultado)