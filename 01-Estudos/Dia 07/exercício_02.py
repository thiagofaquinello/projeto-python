def ler_idade():
    while True:
        try:
            idade = int(input("Informa a idade:"))
            if idade<0:
                print("Valor inválido.")
            else:
                return idade
        except ValueError:
            print("Valor inválido.")

print(ler_idade())