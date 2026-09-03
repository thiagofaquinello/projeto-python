def validar_nota(nota):

    if nota >10 or nota<0:
        return False
    return True

def classificar_nota(nota):

    if validar_nota(nota):
        if nota >= 7:
            return "Aprovado"
        elif nota >= 5 and nota<7:
            return "Recuperação"
        else:
            return "Reprovado"
    return "Nota inválida."


nota = float(input("Digite a nota a ser analisada: "))
resultado = classificar_nota(nota)
print(resultado)