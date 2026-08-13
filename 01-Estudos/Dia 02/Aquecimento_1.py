x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
z = int(input("Digite o terceiro número:"))
w = int(input("Digite o quarto número:"))
k = int(input("Digite o quinto número:"))

if x>=y and x>=z and x>=w and x>=k:
    print(x, "é o maior")
elif y>=x and y>=z and y>=w and y>=k:
    print(y, "é o maior")
elif z>=x and z>=y and z>=w and z>=k:
    print(z, "é o maior")
elif w>=x and w>=z and w>=y and w>=k:
    print(w, "é o maior")
else :
    print(k, "é o maior")



