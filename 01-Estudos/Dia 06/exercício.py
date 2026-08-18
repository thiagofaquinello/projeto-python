def ler_numero():
    while True:
        try:
            numero = float(input("Digite um número:"))
            return numero
        except ValueError:
            print("Entrada inválida.")

print("Número válido:", ler_numero())
    