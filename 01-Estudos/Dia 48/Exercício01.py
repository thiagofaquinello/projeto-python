def aplicar_operacao(valor, operacao):
    return operacao(valor)
dobro = lambda valor: valor*2
adiciona = lambda valor: valor +10
resultado1 = aplicar_operacao(5, dobro)
resultado2 = aplicar_operacao(5, adiciona)
print(resultado1)
print(resultado2)



