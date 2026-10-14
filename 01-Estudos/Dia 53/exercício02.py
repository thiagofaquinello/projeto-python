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

resultado = [processar_registro(r) for r in registros]

import pprint
pprint.pprint(resultado)
