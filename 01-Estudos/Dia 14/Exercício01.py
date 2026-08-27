import json

alunos = [
    {"nome": "Thiago", "nota": 8.5},
    {"nome": "Pedro", "nota": 7.0},
    {"nome": "Ana", "nota": 9.2}
]

def salvar_alunos(alunos):
    with open("alunos.json", "w") as arquivo:
        json.dump(alunos, arquivo)

def carregar_alunos():
    with open("alunos.json","r") as arquivo:
        retorno = json.load(arquivo)
        return retorno

salvar_alunos(alunos)
print(carregar_alunos())