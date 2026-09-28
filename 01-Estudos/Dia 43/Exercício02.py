def aplicar_desconto(percentual, *precos):
    aplicado = []
    for preco in precos:
        resultado = (1-(percentual/100))*preco
        aplicado.append(resultado)
    return aplicado

valores = aplicar_desconto(10, 100, 200, 500)
print(valores)