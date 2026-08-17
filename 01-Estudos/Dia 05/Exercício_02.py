pessoas = []
def cadastro_de_pessoas():
    
     nome = input("Digite o nome da pessoa: ")  
     pessoas.append(nome)
     
def lista_de_nomes():
     if len(pessoas) == 0:
        print("Nenhum pessoa cadastrado.")
        return
     for pessoa in pessoas:
        print(pessoa)

def invalido():
     print("Opção inválida.")

while True:
    opcao = int(input("Digite 1 para cadastrar uma pessoa. \nDigite 2 para listar as pessoas. \nDigite 3 para sair. \n"))

    if opcao == 1 :
        cadastro_de_pessoas() 
    elif opcao == 2 :
        lista_de_nomes()
    elif opcao == 3 :
        break
    else:
            invalido()
    