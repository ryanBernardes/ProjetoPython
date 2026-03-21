#Declaração de variáveis
n1: int = 0
n1: int = 0
s: int = 0
i: int = 0
maior: int = 0
menor: int = 0

#Início
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for i in range(menor,maior+1):
    if i % 2 != 0:
        s = s+i

print("o resultado da somatória dos números ímpares entre esses valores é",s)



#Fim
