a = 0
b = 1 
c = 0 
f = 1
n = int(input("Digite um número para ver a série de Fibonacci até o Nnésimo termo: "))

for i in range(1, n+1):
    print (a,"")
    c = a+b
    a = b
    b = c

