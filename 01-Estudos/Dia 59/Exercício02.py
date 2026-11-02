historico_teste = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5}
]

leituras_teste = [
    {"sensor": "B", "temperatura": "90.0"},
    {"sensor": "C", "temperatura": 76},
    {"sensor": "D", "temperatura": "abc"}
]

def validar_temperatura(entrada):
    try:
        valor_float = float(entrada)
        if 0 <= valor_float <= 100:
            return valor_float  
        return None
    except (ValueError, TypeError):
        return None
    
def atualizar_historico(historico_teste, leituras_teste):
    
    for nova_leitura in leituras_teste:
        if validar_temperatura(nova_leitura["temperatura"])!= None:
            result = validar_temperatura(nova_leitura["temperatura"])
            encontrado = False
            for leitura in historico_teste:
                if leitura["sensor"]==nova_leitura["sensor"]:
                    leitura["temperatura"]=result
                    encontrado = True
                    break
            if not encontrado:
                n_l = {"sensor": nova_leitura["sensor"], "temperatura": result}
                historico_teste.append(n_l)
    
    return historico_teste
resultado = atualizar_historico(historico_teste, leituras_teste)
assert len(historico_teste)==3
assert historico_teste[0]["temperatura"]==72
assert historico_teste[1]["temperatura"]==90
assert historico_teste[2]["temperatura"]==76
assert historico_teste[3]["sensor"]=="D"



