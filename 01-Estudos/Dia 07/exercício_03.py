pessoas = [
    {"nome": "Ana", "idade": 11},
    {"nome": "Bruno", "idade": 25},
    {"nome": "Carla", "idade": 15},
    {"nome": "Diego", "idade": 30},
    {"nome": "Elena", "idade": 22}
]
def maiores_de_idade(pessoas):
        for pessoa in pessoas:
            if pessoa["idade"]>=18:
                idade = pessoa["idade"]
                print(pessoa["nome"], idade)

maiores_de_idade(pessoas)