produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8}
]

def listar_produtos(produtos):
     for produto in produtos:
             print(produto["nome"], "- R$",produto["preco"], "- Estoque:",produto["estoque"])
def mudar_estoque(produtos, operacao):
    nome = input("Digite o produto a ser procurado: ")
    encontrou = False
    for produto in produtos:
        if nome == produto["nome"]:
            print("Quantidade: ",produto["estoque"])
            quantidade = int(input("Digite a alteração no estoque do produto: "))
            if operacao == 1:     
                if quantidade<0:
                    print("Quantidade inválida.")
                    return
                else:
                    produto["estoque"]= produto["estoque"]+quantidade
                    print("Alteração realizada", produto)
            elif operacao == 2:     
                if quantidade<0:
                    print("Quantidade inválida.")
                    return
                elif produto["estoque"] - quantidade < 0:
                    print("Estoque insuficiente.")
                    return
                else:
                    produto["estoque"]= produto["estoque"]-quantidade
                    print("Alteração realizada", produto)
            encontrou = True
                
    if encontrou == False:
        print("Produto não encontrado.")
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
def alterar_preco(produtos):
    nome = input("Digite o produto a ser procurado: ")
    encontrou = False
    for produto in produtos:
        if nome == produto["nome"]:
            novo_preco = verificar_preco()
            produto["preco"]= novo_preco
            print("Alteração realizada", produto)
            encontrou = True
                 
    if encontrou == False:
        print("Produto não encontrado.")
while True:
    try:
        opcao = int(input("1 - Listar produtos\n"
                          "2 - Adicionar estoque\n"
                          "3 - Remover estoque\n"
                          "4 - Alterar preço\n"
                          "5 - Sair\n"
                          "Digite a opção: "))
        if opcao == 1 :
            listar_produtos(produtos)
        elif opcao == 2 :
             operacao = 1
             mudar_estoque(produtos, operacao)
        elif opcao == 3 :
             operacao = 2
             mudar_estoque(produtos, operacao)
        elif opcao == 4 :
             alterar_preco(produtos)
        elif opcao == 5 :
            break
        else:
            print("Opção inválida.")
    except ValueError:
            print("Entrada inválida.")