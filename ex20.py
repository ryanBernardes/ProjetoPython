import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Não é uma equação do 2º grau")

else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existem raízes reais")

    elif delta == 0:
        x = -b / (2*a)
        print("Existe uma raiz real:", x)

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("Existem duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)