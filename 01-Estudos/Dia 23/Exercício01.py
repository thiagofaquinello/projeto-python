produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def verificar_preco(produto):

    if produto["preco"] > 0:
        return True
    return False

def aplicar_desconto(produto, desconto):

    resultado = verificar_preco(produto)
    if resultado is not False:
        produto["preco"] = produto["preco"]*((100-desconto)/100)
        return True
    return False
    
    
def buscar_produto(produtos, nome):

    for produto in produtos:
        if produto["nome"]==nome:
            return produto
    return None 

nome = input("Digite o nome do produto: ")
produto = buscar_produto(produtos, nome)
desconto = float(input("Digite a quantidade de desconto: "))
if aplicar_desconto(produto, desconto): 
    print(produto)
else:
    print("Preço inválido.")