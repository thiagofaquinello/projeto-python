def verificar_aprovacao(media) :
    if media>=6:
        return "Aluno aprovado"
    else :
        return "Aluno reprovado"
       
media = float(input("Digite a média nota: "))


print(verificar_aprovacao(media))