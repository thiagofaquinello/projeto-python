while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0 or nota > 10:
        print("Número inválido.")
    else :
        print("nota = ",nota)
        break