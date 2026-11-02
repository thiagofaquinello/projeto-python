def validar_temperatura(entrada):
    try:
        valor_float = float(entrada)
        if 0 <= valor_float <= 100:
            return valor_float  
        return None
    except (ValueError, TypeError):
        return None

assert validar_temperatura("90.0") == 90.0
assert validar_temperatura(25) == 25.0
assert validar_temperatura(0) == 0.0
assert validar_temperatura(100) == 100.0
assert validar_temperatura("abc") is None
assert validar_temperatura(-5) is None
assert validar_temperatura(101) is None
assert validar_temperatura(None) is None