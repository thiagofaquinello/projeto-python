numeros = [4, 7, 10, 13, 16, 19]

def dobrar_pares(numeros):
   
    return  [numero*2 for numero in numeros if numero%2==0]
resultado = dobrar_pares(numeros)
print(resultado)