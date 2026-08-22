notas = []

def menu():
    print("1 - Adicionar nota\n"
    "2 - Listar notas\n"
    "3 - Mostrar maior nota\n"
    "4 - Mostrar média\n"
    "5 - Mostrar quantidade de aprovados\n"
    "6 - Sair\n")
def adicionar_nota():
     nota = verificarnota()
     notas.append(nota)
def verificarnota():
    while True:
            try:
                nota = float(input("digite a nota do aluno: "))
                if nota < 0 or nota >10:
                    print("Nota inválida.", "\n")
                else:
                    break
            except ValueError:
                print("Entrada inválida.", "\n")
    return nota
def lista_de_notas():
     if len(notas) == 0:
        print("Nenhum aluno cadastrado.", "\n")
        return
     for nota in notas:
        print(nota)
def maior_nota(notas):
    if len(notas) == 0:
        print("Nenhum aluno cadastrado.", "\n")
        return
    maior_nota = 0
    for nota in notas:
        valor = nota
        if valor>maior_nota:
            maior_nota=valor
    print("A maior nota é:", maior_nota, "\n")
def media(notas):
    if len(notas) == 0:
        print("Nenhum aluno cadastrado.", "\n")
        return
    soma = 0
    for nota in notas:
        soma+=nota
    média = soma/len(notas)
    return média
def aprovados(notas):
    aprovados = 0
    for nota in notas:
        if nota>=6:
            aprovados+=1
    print("Aprovados: ",aprovados, "\n")
def invalido():
     print("Opção inválida.\n")
while True:
    try:
        menu()
        opcao = int(input("Digite a opção: "))

        if opcao == 1 :
            adicionar_nota()
        elif opcao == 2 :
            lista_de_notas()
        elif opcao == 3 :
            maior_nota(notas)
        elif opcao == 4 :
            resultado = media(notas)
            print("A média das notas é:", resultado)
        elif opcao == 5 :
            aprovados(notas)
        elif opcao == 6 :
            break
        else:
            invalido()
    except ValueError:
        print("Entrada inválida.")





