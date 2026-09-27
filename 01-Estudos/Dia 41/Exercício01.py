produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 10},
    {"nome": "Sensor", "preco": 250, "estoque": 3},
    {"nome": "Arduino", "preco": 180, "estoque": 8},
    {"nome": "CLP", "preco": 3200, "estoque": 2}
]

def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto  
    return None

def calcular_valor_produto(produto):
    
    return produto["preco"]*produto["estoque"]

def analisar_produto(produtos, nome):

    dicproduto = buscar_produto(produtos, nome)
    if dicproduto:
        valor_estoque = calcular_valor_produto(dicproduto)
        return valor_estoque
    return None
    
nome = input("Digite o nome do produto: ")
resultado = analisar_produto(produtos, nome)
print(resultado)