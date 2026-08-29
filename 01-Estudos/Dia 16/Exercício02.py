motor = {
    "nome": "Motor A",
    "preco": 1500,
    "estoque": 10
}

def aplicar_desconto(motor, percentual):
    motor["preco"] = motor["preco"]*((100-percentual)/100)
    return motor


percentual = float(input("Digite o percentual de redução: "))
resultado = aplicar_desconto(motor, percentual)
print(resultado)