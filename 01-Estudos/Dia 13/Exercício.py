produtos = [
    {"nome": "Motor", "preco": 1500, "estoque": 3},
    {"nome": "Sensor", "preco": 250, "estoque": 12},
    {"nome": "Arduino", "preco": 180, "estoque": 8}
]

arquivo = open("produtos.txt", "a+")
def verificar_arquivo():
    arquivo.seek(0)
    conteudo = arquivo.read()
    if conteudo == "":
        salvar_produtos(produtos)
    else:
        print("Produtos já cadastrados.")
def salvar_produtos(produtos):
    for produto in produtos:
        arquivo.write(produto["nome"]+" "+str(produto["preco"])+" "+str(produto["estoque"])+"\n")

def carregar_produtos():
    lista_produtos=[]
    arquivo.seek(0)
    conteudo = arquivo.read()
    if conteudo == "":
        print("Nenhum produto cadastrado.")
        return
    else:
        linhas = conteudo.splitlines()
        
        for linha in linhas:
            if linha.strip() != "":
                partes = linha.split(" ")
                
                nome = str(partes[0])
                preco = float(partes[1])
                estoque = int(partes[2])

                produto ={"nome": nome, "preco": preco, "estoque": estoque}
                lista_produtos.append(produto)
        return lista_produtos
        

verificar_arquivo()
print(carregar_produtos())

arquivo.close()