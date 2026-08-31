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

def produtos_estoque_baixo(resultado, limite):

    estoque_abaixo_do_limite = []
    for produto in resultado:
        if produto["estoque"] < limite:
            estoque_abaixo_do_limite.append(produto)
    return estoque_abaixo_do_limite

def calcular_valor_total(resultado):

    valor_total = 0
    for produto in resultado:
        valor_total += produto["preco"]*produto["estoque"]
    return valor_total

resultado = carregar_produtos()

while True:
    try:
        opcao = int(input("1 - Listar produtos \n2 - Mostrar produtos com estoque baixo \n3 - Mostrar valor total do estoque \n4 - Sair \nDigite a opção:"))

        if opcao == 1:
            print(resultado)
        elif opcao == 2:
            limite = int(input("Digite o limite crítico para estoque: "))
            estoque_baixo = produtos_estoque_baixo(resultado, limite)
            print(f"Os produtos com estoque baixo são: {estoque_baixo}")
        elif opcao == 3:
            valor = calcular_valor_total(resultado)
            print(f"O valor total do estoque é: {valor}")
        elif opcao == 4:
            break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")