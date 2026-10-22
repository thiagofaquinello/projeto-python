historico = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5},
    {"sensor": "C", "temperatura": 65.0}
]

novas_leituras = [
    {"sensor": "B", "temperatura": "90.0"},
    {"sensor": "D", "temperatura": 76},
    {"sensor": "E", "temperatura": "abc"},
    {"sensor": "F", "temperatura": -5},
    {"sensor": "G", "temperatura": 82}
]

import json

arquivo_destino = "dados_sensores.json"

def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo) 

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            retorno = json.load(arquivo)
            return retorno
    except FileNotFoundError:
        return []
    
resultado = carregar_dados(arquivo_destino)

if not resultado:
    resultado = historico.copy()

def validar_temperatura(entrada):
    try:
        valor_float = float(entrada)
        if 0 <= valor_float <= 100:
            return valor_float  
        return None
    except (ValueError, TypeError):
        return None

def atualizar_historico(historico, novas_leituras):
    
    for nova_leitura in novas_leituras:
        if validar_temperatura(nova_leitura["temperatura"])!= None:
            result = validar_temperatura(nova_leitura["temperatura"])
            encontrado = False
            for leitura in historico:
                if leitura["sensor"]==nova_leitura["sensor"]:
                    leitura["temperatura"]=result
                    encontrado = True
                    break
            if not encontrado:
                n_l = {"sensor": nova_leitura["sensor"], "temperatura": result}
                historico.append(n_l)
    
    return historico

resultado = atualizar_historico(resultado, novas_leituras)
salvar_dados(resultado, arquivo_destino)

print(resultado)