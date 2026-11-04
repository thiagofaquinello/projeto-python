from historico import atualizar_historico


historico = [
    {"sensor": "A", "temperatura": 72.0},
    {"sensor": "B", "temperatura": 88.5}
]

novas_leituras = [
    {"sensor": "B", "temperatura": 90.0},
    {"sensor": "C", "temperatura": 76.0}
]

resultado = atualizar_historico(historico,novas_leituras)
print(resultado)