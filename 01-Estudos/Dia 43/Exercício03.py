def analisar_leituras(limite, *leituras):
    if leituras:
        contador = 0
        maior = leituras[0]
        contador_acima_limite = 0
        for leitura in leituras:
            contador += 1
            if leitura>limite:
                contador_acima_limite += 1
            if leitura > maior:
                maior = leitura
        return {"quantidade": contador,"acima_limite": contador_acima_limite,"maior_leitura": maior}
    return {"quantidade": 0,"acima_limite": 0,"maior_leitura": None}

resultado = analisar_leituras(50, 42, 55, 61, 48, 70)
print(resultado)