leituras = [42, 57, 63, 48, 71, 55]

def processar_leituras(leituras, transformacao, condicao):
    lista = []
    for leitura in leituras:
        result1 = transformacao(leitura)
        result2 = condicao(result1)
        if result2:
            lista.append(result1)
    return lista
transformacao = lambda leitura: ((leitura-32)*5)/9
condicao = lambda result1: result1>20
resultado = processar_leituras(leituras, transformacao, condicao)
print(resultado)