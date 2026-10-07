leituras = [42, 57, 63, 48, 71, 55]

leitura_acima_de_70 = any(leitura>70 for leitura in leituras)
todas_maiores_que_40 = all(leitura>40 for leitura in leituras)
todas_menores_que_80 = all(leitura<80 for leitura in leituras)

print(leitura_acima_de_70)
print(todas_maiores_que_40)
print(todas_menores_que_80)