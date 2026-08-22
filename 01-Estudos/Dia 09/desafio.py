produtos = []

def cadastro_de_produtos():

    produto = input("Digite o produto: ")
    preco = verificar_preco()
    produtos.append({"produto": produto, "preco": preco})

def verificar_preco():
    while True:
            try:
                preco = float(input("digite o preço do produto: "))
                if preco < 0:
                    print("Preço inválido.")
                else:
                    break
            except ValueError:
                print("Entrada inválida.")
    return preco

def lista_de_produtos():
     if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
     for produto in produtos:
        print(produto["produto"])

def maior_preco(produtos):

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    maior_preco = 0
    maiores_produtos = []
    for produto in produtos:
        valor = produto["preco"]
        if valor>maior_preco:
            maior_preco = valor
            maiores_produtos.clear()
            maiores_produtos.append(produto)
        elif valor == maior_preco:
            maiores_produtos.append(produto)
    for produto in maiores_produtos:
        print("O produto mais caro é:", produto["produto"], "- Preço:", maior_preco)

def media_dos_precos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    soma = 0
    for produto in produtos:
        soma += produto["preco"]
    media=soma/len(produtos)
    return media

def buscar_produto(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    encontrou = False
    palavra = input("Digite o produto desejado: ")
    for produto in produtos:
        if produto["produto"]== palavra:
            print(palavra, "- R$" ,produto["preco"])
            encontrou = True
            return
    if encontrou == False:
        print("Produto não encontrado.")

while True:
    try:
        opcao = int(input("1 - Cadastrar produto\n"
                          "2 - Listar produtos\n"
                          "3 - Mostrar produto mais caro\n"
                          "4 - Mostrar preço médio\n"
                          "5 - Buscar produto\n"
                          "6 - Sair\n"
                          "Digite a opção: "))
        if opcao == 1 :
            cadastro_de_produtos()
        elif opcao == 2 :
            lista_de_produtos()
        elif opcao == 3 :
            maior_preco(produtos)
        elif opcao == 4 :
            print(media_dos_precos(produtos))
        elif opcao == 5 :
            buscar_produto(produtos)
        elif opcao == 6:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")

