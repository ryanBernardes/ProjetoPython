
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if(n1 > n2):
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

for i in range(menor, maior + 1):
    if (i>1):
        nP = 0
        for j in range(1, i + 1):
            if i % j==0:
                nP += 1

        if nP == 2:
            print(i)
    




