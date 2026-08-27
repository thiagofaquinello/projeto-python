import json

def cadastrar_alunos(alunos):
    
    salva_alunos = alunos
    nome = input("Digite o nome do aluno: ")
    nota = verificarnota()
    salva_alunos.append({"nome": nome, "nota": nota})
    with open("salva_alunos.json", "w") as arquivo:
        json.dump(salva_alunos, arquivo)

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

def listar_alunos():

    try:
        with open("salva_alunos.json","r") as arquivo:
            try:
                retorno = json.load(arquivo)
                return retorno
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

def media_turma(alunos):
    if len(alunos) == 0:
        return 0
    soma=0
    for aluno in alunos:
        soma += aluno["nota"]
    media=soma/len(alunos)
    return media

alunos = listar_alunos()

while True:
    try:
        opcao = int(input("1 - Listar alunos\n"
                          "2 - Adicionar aluno\n"
                          "3 - Média da turma\n"
                          "4 - Sair\n"
                          "Digite a opção: "))

        if opcao == 1:
            print(alunos)
        elif opcao == 2:
            cadastrar_alunos(alunos)
        elif opcao == 3:
            print(media_turma(alunos))
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida")
