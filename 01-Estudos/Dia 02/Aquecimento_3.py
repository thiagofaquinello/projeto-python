x=input("digite a palavra:")
palavra = x
soma = 0
for letra in palavra:
    if letra in "aeiou":
        soma+=1
print(soma)

