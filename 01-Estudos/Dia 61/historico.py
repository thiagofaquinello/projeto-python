from validacao import validar_temperatura

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