lista = [10,20,30,60,10]
def maior_numero(lista):
    valor = lista[0]
    for num in lista:
        if num>=valor:
            valor = num
    return valor

print(maior_numero(lista))
