leituras = [12, 18, 15, 21, 14]

def analisar_leituras(*leituras):
    soma = 0
    contador = 0
    maior=leituras[0]
    menor=leituras[0]
    for leitura in leituras:
        soma += leitura
        contador+=1
        if leitura>maior:
            maior=leitura
        if leitura<menor:
            menor=leitura
    media = soma/contador
    return {"Quantidade de leituras": contador,"maior leitura": maior, "menor leitura": menor, "media": media}

resultado = analisar_leituras(*leituras)
print(resultado)
