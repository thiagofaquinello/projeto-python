alunos = []
def cadastrodealunos():
    
     nome = input("Digite o nome do aluno: ")
     nota1 = verificarnota()
     nota2 = verificarnota()
     alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2})

def verificarnota():
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

def listadenomes():
     if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
     for aluno in alunos:
        print(aluno["nome"])
def media(aluno):
    media = (aluno["nota1"]+aluno["nota2"])/2
    return media

def mostrar_media():
     if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
     for aluno in alunos:
        print(aluno["nome"],"- Média =", media(aluno)) 
def resultado():
     if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
     for aluno in alunos:
        if media(aluno) < 6:
            print(aluno["nome"], "reprovado")
        else:
            print(aluno["nome"], "aprovado")
def invalido():
     print("Opção inválida.")


while True:
    try:
        opcao = int(input("Digite 1 para cadastrar o aluno. \nDigite 2 para listar os alunos. \nDigite 3 para ver a média dos alunos. \nDigite 4 para ver a situação dos alunos. \nDigite 5 para sair do programa.\nDigite a opção:"))

        if opcao == 1 :
            cadastrodealunos() 
        elif opcao == 2 :
            listadenomes()
        elif opcao == 3 :
            mostrar_media()
        elif opcao == 4 :
            resultado()
        elif opcao == 5 :
            break
        else:
            invalido()
    except ValueError:
        print("Entrada inválida.")