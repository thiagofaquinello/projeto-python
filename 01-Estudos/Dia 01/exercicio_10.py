x = float(input("Digite o primeiro número"))
y = float(input("Digite o segundo número"))
z = input("Digite a operação")

if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/" and y == 0:
    print("conjunto vazio")
elif z == "/":
    print(x/y)
else:
    print("Inválido")

