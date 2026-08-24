produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def alterar_preco(produtos):
    nome = input("Digite o produto a ser procurado: ")
    encontrou = False
    for produto in produtos:
        if nome == produto["nome"]:
            novo_preco = float(input("Digite o novo preço do produto: "))
            produto["preco"]= novo_preco
            print("Alteração realizada", produto)
            encontrou = True
            
    if encontrou == False:
        print("Produto não encontrado.")
          

alterar_preco(produtos)