import math
#Declaração de variáveis
c1: float = 0
c2: float = 0
h: float = 0

#Início
c1 = float(input("digite o valor do cateto 1: "))
c2 = float(input("digite o valor do cateto 2: "))

h = math.sqrt((c1*c1)+(c2*c2))
print ("O valor da Hipotenusa é :",h)


#Fim
