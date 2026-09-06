def calcular_desconto(preco, percentual):
    if percentual < 0 or 100-percentual<0:
        return False
    if preco < 0:
        return False
    valor_final = preco*(percentual/100)
    return valor_final
preco = float(input("Digite o preço: \n"))
percentual = float(input("Digite a porcentagem de desconto: \n"))
if calcular_desconto(preco, percentual):
    print(f"O valor descontado é: {calcular_desconto(preco, percentual)}")
else:
    print("Entrada inválida.")