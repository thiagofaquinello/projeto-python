temperaturas = [20, 25, 30, 35, 40]

def converter_temperaturas(temperaturas):
    i=0
    for temperatura in temperaturas:
        temperatura = ((temperatura*9)/5)+32
        temperaturas[i]=temperatura
        i+=1
    return temperaturas

print(converter_temperaturas(temperaturas))

