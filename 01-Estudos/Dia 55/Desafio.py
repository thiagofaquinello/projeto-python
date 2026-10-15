novas_leituras = [
    {"sensor": "A", "temperatura": "74.5"},
    {"sensor": "B", "temperatura": "abc"},
    {"sensor": "C", "temperatura": 91},
    {"sensor": "D", "temperatura": -5},
    {"sensor": "E", "temperatura": 68},
    {"sensor": "F", "temperatura": "79"}
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

def validar_temperatura(entrada):
    try:
        valor_float = float(entrada)
        if 0 <= valor_float <= 100:
            return valor_float  
        return None
    except (ValueError, TypeError):
        return None

def processar_registro(registro):
    id_sensor = registro.get("sensor")
    temp_original = registro.get("temperatura")
    temp_validada = validar_temperatura(temp_original)
    e_valido = temp_validada is not None
    return {
        "sensor": id_sensor, 
        "temperatura": temp_validada, 
        "validade": e_valido
    }

resultado1 = [processar_registro(r) for r in novas_leituras]
lista_válidos = [valor for valor in resultado1 if valor["validade"]]
sensores_existentes = {item["sensor"] for item in resultado}

lista_para_adicionar = [
    sensor for sensor in lista_válidos 
    if sensor["sensor"] not in sensores_existentes
]

resultado.extend(lista_para_adicionar)
salvar_dados(resultado, arquivo_destino)

print(resultado)