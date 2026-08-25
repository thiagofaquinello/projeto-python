vendas = [
    {"produto": "Motor", "quantidade": 3, "preco": 1500},
    {"produto": "Sensor", "quantidade": 10, "preco": 250},
    {"produto": "Arduino", "quantidade": 5, "preco": 180},
    {"produto": "CLP", "quantidade": 2, "preco": 3200}
]

def calcular_total(venda):
    return venda["quantidade"] * venda["preco"]

def analisar_vendas(lista_vendas):
    faturamento_total = 0
    maior_faturamento = 0
    produto_top = ""

    for venda in lista_vendas:
        total_venda = calcular_total(venda)
        
        faturamento_total += total_venda
        
        if total_venda > maior_faturamento:
            maior_faturamento = total_venda
            produto_top = venda["produto"]

    return faturamento_total, produto_top

total, campeao = analisar_vendas(vendas)

print(f"Faturamento total: R$ {total:.2f}")
print(f"Produto com maior faturamento: {campeao}")