def calcular_desconto(preco, percentual):
    if percentual < 0 or percentual > 100:
        return False
    if preco < 0:
        return False
    valor_descontado = preco*(percentual/100)
    return valor_descontado
def calcular_preco_final(preco, percentual):
    desconto = calcular_desconto(preco, percentual)

    if desconto is False:
        return False

    return preco - desconto
preco = float(input("Digite o preço: \n"))
percentual = float(input("Digite a porcentagem de desconto: \n"))
valor = calcular_preco_final(preco, percentual)
if valor is not False:
    print(f"O valor final é: {valor}")
else:
    print("Entrada inválida.")