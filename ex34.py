#Declaração de variáveis
n: int = 0
i: int = 0
t: int = 0
#Início
n = int(input("Insira um número para ver a sua tabuada: "))
for i in range(1,11,1):
    t = n*i
    print(n,"X",i,"=",t)



#Fim
