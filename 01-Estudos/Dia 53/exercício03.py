registros = [
    {"sensor": "A", "temperatura": "72"},
    {"sensor": "B", "temperatura": "abc"},
    {"sensor": "C", "temperatura": 105},
    {"sensor": "D", "temperatura": "88.5"},
    {"sensor": "E"},
]

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

def analisar_registros(registros):
    resultados_processados = [processar_registro(r) for r in registros]
    
    total_registros = len(resultados_processados)
    quantidade_validos = 0
    quantidade_invalidos = 0
    temperaturas_validas = []
    
    for analise in resultados_processados:
        if analise["validade"]:
            quantidade_validos += 1
            temperaturas_validas.append(analise["temperatura"])
        else:
            quantidade_invalidos += 1
            
    if quantidade_validos > 0:
        media_temperaturas = sum(temperaturas_validas) / quantidade_validos
    else:
        media_temperaturas = None
        
    return {
        "total_registros": total_registros,
        "quantidade_validos": quantidade_validos,
        "quantidade_invalidos": quantidade_invalidos,  
        "temperaturas_validas": temperaturas_validas,
        "media_temperaturas": media_temperaturas
    }

resultado = analisar_registros(registros)

print(resultado)
