import json

produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def salvar_produtos(produtos):
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo)

def carregar_produtos():
    
    try:
        with open("produtos.json","r") as arquivo:
            retorno = json.load(arquivo)
            return retorno
    except FileNotFoundError:
        salvar_produtos(produtos)
        with open("produtos.json","r") as arquivo:
            retorno = json.load(arquivo)
            return retorno

def buscar_produto(resultado, nome):

    for produto in resultado:
        if produto["nome"]==nome:
            return produto
    return None

def alterar_preco(resultado_nome, novo_preco):

    resultado_nome["preco"] = novo_preco
    return resultado_nome

resultado = carregar_produtos()

while True:
    try:
        opcao = int(input("1 - Listar produtos \n2 - Alterar preço \n3 - Sair \nDigite a opção:"))

        if opcao == 1:
            print(resultado)
        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            resultado_nome = buscar_produto(resultado, nome)
            if resultado_nome is not None:
                novo_preco = float(input("Digite o novo preço: "))
                alteracao = alterar_preco(resultado_nome, novo_preco)
                with open("produtos.json", "w") as arquivo:
                    json.dump(resultado, arquivo)
                print(alteracao)
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")



