arquivo = open("notas.txt", "a+")
def adicionar_notas():
    nota = verificar_nota()
    arquivo.write(str(nota)+"\n")

def verificar_nota():

    while True:
            try:
                nota = float(input("digite a nota do aluno: "))
                if nota < 0 or nota >10:
                    print("Nota inválida.")
                else:
                    break
            except ValueError:
                print("Entrada inválida.")
    return nota

def Listar_notas():
    arquivo.seek(0)
    conteudo = arquivo.read()
    if conteudo == "":
        print("Nenhum aluno cadastrado.")
        return
    else:
        print(conteudo)
            


while True:
    try:
        opcao = int(input("1 - Adicionar nota\n"
                          "2 - Listar notas\n"
                          "3 - Sair\n"
                          "Digite a opção: "))
        if opcao == 1:
            adicionar_notas()
        elif opcao == 2:
            Listar_notas()
        elif opcao == 3:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")

arquivo.close()