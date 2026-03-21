#Declaração de variáveis
n: int = 0
f: int = 1
i: int = 0

#Início
n = int(input("Insira um número inteiro para descobrir seu fatorial: "))
for i in range(1,n+1):
    f = f*i
    

print(f)

#Fim
