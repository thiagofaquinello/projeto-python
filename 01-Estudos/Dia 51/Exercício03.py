motores = [
    {"nome": "Motor A", "temperatura": 72, "limite": 80},
    {"nome": "Motor B", "temperatura": 91, "limite": 85},
    {"nome": "Motor C", "temperatura": 68, "limite": 70},
    {"nome": "Motor D", "temperatura": 103, "limite": 90},
    {"nome": "Motor E", "temperatura": 77, "limite": 75},
]

algum_acima_limite = any(motor["temperatura"]>motor["limite"] for motor in motores)
todos_abaixo_110 = all(motor["temperatura"]<110 for motor in motores)
motores_acima_limite = [motor for motor in motores if motor["temperatura"]>motor["limite"]]
print(algum_acima_limite )
print(todos_abaixo_110)
print(motores_acima_limite)