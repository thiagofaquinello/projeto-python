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

def melhordaturma(alunos):

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    maior_media = 0
    melhores_alunos = []
    for aluno in alunos:
        valor = media(aluno)
        if valor>maior_media:
            maior_media = valor
            melhores_alunos.clear()
            melhores_alunos.append(aluno)
        elif valor == maior_media:
            melhores_alunos.append(aluno)
    for aluno in melhores_alunos:
        print("Melhor aluno:", aluno["nome"], "- Média", maior_media)

def estatisticas(alunos):

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print("Alunos cadastrados: ",len(alunos))
    soma = 0
    reprovados = 0
    aprovados = 0
    for aluno in alunos:
        valor = media(aluno)
        soma += valor
        if valor < 6:
            reprovados += 1
        else:
            aprovados += 1
    média = soma/len(alunos)
    print("Média da turma: ",média)
    print("Aprovados: ",aprovados)
    print("Reprovados: ", reprovados)

def invalido():
     
     print("Opção inválida.")


while True:
    try:
        opcao = int(input("Digite 1 para cadastrar o aluno. \nDigite 2 para listar os alunos. \nDigite 3 para ver a média dos alunos. \nDigite 4 para ver a situação dos alunos. \nDigite 5 para ver o melhor aluno. \nDigite 6 para ver as estatísticas da turma. \nDigite 7 para sair do programa. \nDigite a opção:"))

        if opcao == 1 :
            cadastrodealunos()
        elif opcao == 2 :
            listadenomes()
        elif opcao == 3 :
            mostrar_media()
        elif opcao == 4 :
            resultado()
        elif opcao == 5 :
            melhordaturma(alunos)
        elif opcao == 6 :
            estatisticas(alunos)
        elif opcao == 7 :
            break
        else:
            invalido()
    except ValueError:
        print("Entrada inválida.")