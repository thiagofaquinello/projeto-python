def aprovacao(a,b):
    if (a+b)/2>=6:
        resultado = "aprovado"
    else :
        resultado = "reprovado"
    return resultado 

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print(aprovacao(a, b))