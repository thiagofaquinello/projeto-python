def validar_preco(preco):

    if preco < 0:
        return False
    return True

preco = float(input("Digite o preço: "))

resultado = validar_preco(preco)

if resultado == True:
    print("Preço válido")
else:
    print("Preço inválido")