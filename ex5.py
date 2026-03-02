import math

#Declaração de variáveis
raiz1: float = 0
raiz2: float = 0
a: float = 0
b: float = 0
c: float = 0
delta : float = 0

#Início
a = float(input("digite o valor de A:"))
b = float(input("digite o valor de B:"))
c = float(input("digite o valor de C:"))
delta = (b*b) - 4*(a*c)
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

print ("A Raiz 1 é:", raiz1)
print ("A Raiz 2 é:", raiz2)

#Fim

