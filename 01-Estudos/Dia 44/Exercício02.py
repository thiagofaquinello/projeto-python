def mostrar_dados(**dados):
    lista = []
    for chave in dados:
        valor = dados[chave] 
        lista.append(f"{chave}: {valor}") 
    return lista

resultado = mostrar_dados(
    nome="Motor",
    preco=1500,
    estoque=10
)

print(resultado)
