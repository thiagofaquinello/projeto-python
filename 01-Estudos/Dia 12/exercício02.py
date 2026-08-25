numeros = [0, 5, 8, 0, 3, 7]


def calcular_media(numeros):
    soma = 0
    
    for nota in numeros:
        soma+=nota
    media=soma/len(numeros)
    return media
def verificar_situacao():
    media = calcular_media(numeros)
    if media>=6:
        print("Aluno 1 aprovado.")
    else:
        print("Aluno 1 reprovado.")

verificar_situacao()
    


