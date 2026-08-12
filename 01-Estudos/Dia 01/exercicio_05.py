x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))
z = int(input("Digite o terceiro número:"))

if x>y>z:
    print(x, "é o maior")
elif z>y>x:
    print(z, "é o maior")
elif y>z>x:
    print(y, "é o maior")
elif y>x>z:
    print(y, "é o maior")
elif x>z>y:
    print(x, "é o maior")
elif z>x>y:
    print(z,"é o maior")
elif x>y and y==z:
    print(x, "é o maior")
elif y>x and x==z:
    print(y, "é o maior")
elif z>y and y==x:
    print(z, "é o maior")
elif x==y>z:
    print(x, "é o maior")
elif z==y>x:
    print(z, "é o maior")
elif z==x>y:
    print(z, "é o maior")
else:
    print(x, "é o maior")
     