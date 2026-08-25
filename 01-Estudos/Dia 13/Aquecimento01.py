nomes = ["Thiago", "Pedro", "Nicolas", "Ana", "Maria"]

arquivo = open("nomes.txt", "w")

for nome in nomes:
    arquivo.write(nome+"\n")


arquivo.close()



