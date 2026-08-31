produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def buscar_produto(produtos, nome):

    for produto in produtos:
        if produto["nome"]==nome:
            return produto
    return None

def adicionar_estoque(resultado_nome, quantidade):

    resultado_nome["estoque"] = resultado_nome["estoque"]+quantidade
    return resultado_nome

def remover_estoque(resultado_nome, quantidade):
    if quantidade < 0:
        return False
    if resultado_nome["estoque"]-quantidade<0:
        return False
    else:
        resultado_nome["estoque"] = resultado_nome["estoque"]-quantidade
        return True
    
nome = input("Digite o nome do produto: ")
resultado_nome = buscar_produto(produtos, nome)
if resultado_nome is None:
    print("Produto não localizado no estoque.")
else:
    opcao = int(input("1 - Adicionar estoque \n2 - Remover estoque \nDigite a opção: "))
    if opcao == 1:
        quantidade = int(input("Digite a quantidade recebida ao estoque: "))
        alteracao = adicionar_estoque(resultado_nome, quantidade)
        print(alteracao)
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade retirada do estoque: "))
        alteracao = remover_estoque(resultado_nome, quantidade)
        if alteracao == False:
            print("Quantidade inválida.")
        else:
            print(resultado_nome)
        
    else:
        print("Opção inválida.")
