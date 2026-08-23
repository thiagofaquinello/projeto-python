temperaturas = [23.5, 25.1, 27.8, 30.2, 28.4, 21.9, 26.7]

def analisar_temperaturas(temperaturas):
    valor_max = temperaturas[0]
    valor_min = temperaturas[0]
    soma = 0
    temperaturas_altas = []
    for temperatura in temperaturas:
            soma += temperatura
            if temperatura >= valor_max:
                valor_max = temperatura
            if temperatura <= valor_min:
                valor_min = temperatura
            if temperatura > 27:
                 temperaturas_altas.append(temperatura)
    media = soma/len(temperaturas) 
    return valor_max, valor_min, media, temperaturas_altas 

valor_max, valor_min, media, temperaturas_altas = analisar_temperaturas(temperaturas)
print("A maior temperatura é: ", valor_max)
print("A menor temperatura é: ", valor_min)  
print("A temperatura média é: ", media)  
print("As temperaturas acima de 27 graus são: ", temperaturas_altas)   