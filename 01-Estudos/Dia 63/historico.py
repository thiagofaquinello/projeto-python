from validacao import validar_temperatura

def atualizar_historico(historico_teste, leituras_teste):
    
    for nova_leitura in leituras_teste:
        resulta = validar_temperatura(nova_leitura.get("temperatura"))
        if resulta!= None:
            result = resulta
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

if __name__ == "__main__":
    historico = [
        {"sensor": "A", "temperatura": 72.0}
    ]

    novas_leituras = [
        {"sensor": "A", "temperatura": 90.0},
        {"sensor": "B"},
        {"sensor": "C", "temperatura": "abc"},
        {"sensor": "D", "temperatura": 75.0}
    ]

    resultado = atualizar_historico(historico, novas_leituras)
    print(resultado)