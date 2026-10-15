sensores = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5},
    {"sensor": "C", "temperatura": 65.0}
]

import json

def salvar_dados(dados):
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)
def carregar_dados():
    try:
        with open("dados.json","r") as arquivo:
            retorno = json.load(arquivo)
            return retorno
    except FileNotFoundError:
        return []
salvar_dados(sensores)
resultado = carregar_dados()
print(resultado)

        
