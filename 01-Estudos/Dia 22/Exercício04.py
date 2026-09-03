import json

produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def salvar_produtos(resultado):
    with open("produtos.json", "w") as arquivo:
        json.dump(resultado, arquivo)

def carregar_produtos():
    
    try:
        with open("produtos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        salvar_produtos(produtos)
        return produtos

def buscar_produto(resultado, nome):

    for produto in resultado:
        if produto["nome"]==nome:
            return produto
    return None

def verificar_quantidade(quantidade):
    if quantidade < 0:
        return False
    return True

def adicionar_estoque(resultado_nome, quantidade):
    if verificar_quantidade(quantidade):
        resultado_nome["estoque"] += quantidade
        return True
    return False

def remover_estoque(resultado_nome, quantidade):
    if quantidade < 0:
        return False
    if resultado_nome["estoque"]-quantidade<0:
        return False
    else:
        resultado_nome["estoque"] = resultado_nome["estoque"]-quantidade
        return True

def alterar_preco(resultado_nome, novo_preco):

    resultado_nome["preco"] = novo_preco
    return resultado_nome

def executar_adicao_estoque(resultado):

    nome = input("Digite o nome do produto: ")
    resultado_nome = buscar_produto(resultado, nome)
    if resultado_nome is None:
        print("Produto não localizado no estoque.")
        return 
    quantidade = int(input("Digite a quantidade recebida ao estoque: "))
    alteracao = adicionar_estoque(resultado_nome, quantidade)
    if alteracao == False:
        print("Quantidade inválida.")
    else:
        salvar_produtos(resultado)
        print(resultado_nome)

def selecionar_produto(resultado):

    nome = input("Digite o nome do produto: ")
    return buscar_produto(resultado, nome)

def executar_consulta_estoque(resultado):

    produto = selecionar_produto(resultado)
    if produto is not None:
        print(" Produto:", produto["nome"],"\n","Preço R$ ", produto["preco"],"\n","Estoque:", produto["estoque"])
    else:
        print("Produto não localizado.")

resultado = carregar_produtos()

while True:
    try:
        opcao = int(input("1 - Listar produto \n2 - Adicionar estoque \n3 - Remover estoque \n4 - Alterar preço \n5 - Sair \nDigite a opção:"))

        if opcao == 1:
            executar_consulta_estoque(resultado)
        elif opcao == 2:
            executar_adicao_estoque(resultado)
        elif opcao == 3:
            nome = input("Digite o nome do produto: ")
            resultado_nome = buscar_produto(resultado, nome)
            if resultado_nome is None:
                print("Produto não localizado no estoque.")
                continue
            quantidade = int(input("Digite a quantidade retirada do estoque: "))
            alteracao = remover_estoque(resultado_nome, quantidade)
            if alteracao == False:
                print("Quantidade inválida.")
            else:
                salvar_produtos(resultado)
                print(resultado_nome)
        elif opcao == 4:
            nome = input("Digite o nome do produto: ")
            resultado_nome = buscar_produto(resultado, nome)
            if resultado_nome is None:
                print("Produto não localizado no estoque.")
                continue
            novo_preco = float(input("Digite o novo preço: "))
            alteracao = alterar_preco(resultado_nome, novo_preco)
            salvar_produtos(resultado)
            print(alteracao)
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")