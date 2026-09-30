dados_principais = ["Motor A", "Industrial"]
leituras = [45, 52, 48]
informacoes = {
    "fabricante": "WEG",
    "setor": "Linha 1"
}

def registrar_equipamento(nome, categoria, *leituras, **informacoes):
    contador = 0
    maior = None  
    
    for leitura in leituras:
        if contador == 0:
            maior = leitura
        elif leitura > maior:
            maior = leitura
        contador += 1
        
    return {
        "nome": nome,
        "categoria": categoria,
        "quantidade_leituras": contador,
        "maior_leitura": maior,
        "informacoes": informacoes  
    }

resultado = registrar_equipamento(*dados_principais, *leituras, **informacoes)
print(resultado)
