def eh_par(numero):

    if numero%2==0:
        return True
    return False

def analisar_numero(numero):

    if eh_par(numero) == True:
        return "É par."
    return "É impar"

numero = int(input("Digite o número a ser verificado: "))
resultado = analisar_numero(numero)
print(resultado)