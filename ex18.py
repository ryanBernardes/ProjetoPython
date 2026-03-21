#Declaração de variáveis
n1: int = 0
n2: int = 0
diferenca: int = 0


#Início
n1 = int(input("digite o primeiro número "))
n2 = int(input("digite o segundo número "))

if n1 > n2:
    diferenca = n1 - n2
elif n2 > n1:
    diferenca = n2 - n1

print ("A diferença do maior para o menor é:",diferenca)



#Fim
