#Declaração de variáveis
n: int = 0
s: float = 0
i: int = 0

#Início
n = int(input("Insira um número para ver a série: "))
for i in range(1,n+1):
    s = s+(1/i)
    
print(s)



#Fim
