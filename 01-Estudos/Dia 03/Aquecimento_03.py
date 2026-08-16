pessoas = [{"nome": "Thiago", "idade": 47},{"nome": "Pedro", "idade": 10},{"nome": "João", "idade": 20},{"nome": "Mateus", "idade": 30},{"nome": "Caio", "idade": 27}]
numero=0
nome = ""
for pessoa in pessoas:
    print(pessoa["nome"], pessoa["idade"])
for pessoa in pessoas:
    if pessoa["idade"]>=18:
            print(pessoa["nome"], pessoa["idade"])
for pessoa in pessoas:
    if pessoa["idade"]>= numero:
        numero=  pessoa["idade"]
        nome=pessoa["nome"]
print(nome, numero)
