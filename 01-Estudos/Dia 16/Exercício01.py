temperaturas = [20, 25, 30, 35, 40]

def aumentar_temperaturas(temperaturas):
    for i in range(5):
        temperaturas[i] = temperaturas[i] + 2
        
    return temperaturas

resultado = aumentar_temperaturas(temperaturas)
print(resultado)