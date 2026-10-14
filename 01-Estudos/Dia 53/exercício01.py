def validar_temperatura(entrada):
    try:
        valor_float = float(entrada)
        
        if 0 <= valor_float <= 100:
            return valor_float
        return None
        
    except (ValueError, TypeError):
        return None

entradas_teste = ["85", "abc", -10, 100, None]

resultados = [validar_temperatura(item) for item in entradas_teste]

print(resultados)
