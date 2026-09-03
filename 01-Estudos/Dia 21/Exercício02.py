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

def verificar_quantidade(quantidade):
    if quantidade < 0:
        return False
    return True
def adicionar_estoque(resultado_nome, quantidade):
    if verificar_quantidade(quantidade):
        resultado_nome["estoque"] = resultado_nome["estoque"]+quantidade
        return True
    return False

nome = input("Digite o nome do produto: ")
resultado_nome = buscar_produto(produtos, nome)
if resultado_nome is None:
    print("Produto não localizado no estoque.")
    exit()
quantidade = int(input("Digite a quantidade recebida ao estoque: "))
alteracao = adicionar_estoque(resultado_nome, quantidade)
if alteracao == False:
    print("Quantidade inválida.")
else:
    print(resultado_nome)
