def apresentar(nome, idade, curso):
    return f"{nome} tem {idade} anos e cursa {curso}."

dados = {
    "nome": "Thiago",
    "idade": 19,
    "curso": "Engenharia"
}

resultado = apresentar(**dados)
print(resultado)