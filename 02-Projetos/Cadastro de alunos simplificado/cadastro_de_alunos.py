alunos = []
while True:
    opcao = int(input("Digite 1 para cadastrar o aluno. \nDigite 2 para listar os alunos. \nDigite 3 para ver a média dos alunos. \nDigite 4 para ver a situação dos alunos. \nDigite 5 para sair do programa.\nDigite a opção:"))

    if opcao == 1 :
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("digite a primeira nota do aluno: "))
        nota2 = float(input("digite a segunda nota do aluno: "))  
        alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2})  
    elif opcao == 2 :
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            print(aluno["nome"])
    elif opcao == 3 :
        if len(alunos) == 0:
                    print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            media = (aluno["nota1"]+aluno["nota2"])/2
            print(aluno["nome"],media)
    elif opcao == 4 :
        if len(alunos) == 0:
                    print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            media = (aluno["nota1"]+aluno["nota2"])/2
            if media < 6:
                print(aluno["nome"], "reprovado")
            else:
                print(aluno["nome"], "aprovado")
    elif opcao == 5 :
        break
    else:
        print("Opção inválida.")