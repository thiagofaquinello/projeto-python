def analisar_produto(nome, **dados):
    acumulador = 0
    for chave in dados:
        acumulador += 1
        
    valor_estoque = dados["preco"] * dados["estoque"]
    
    return {
        "nome": nome, 
        "valor estoque": valor_estoque, 
        "estoque baixo": dados["estoque"] < 5, 
        "quantidade de informações": acumulador
    }

resultado = analisar_produto(
    "CLP",
    preco=3200,
    estoque=2
)

print(resultado)
