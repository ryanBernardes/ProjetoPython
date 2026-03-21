
n = int(input("Você ira digitar 100 numeros, e no final ira ver qual foi o maior e o menor: "))
maior = n
menor = n

for i in range(2, 11, 1):
    n = int(input())
    if (n>maior):
        maior = n

    if (n<menor):
        menor = n

print("O maior número foi:",maior,"e o menor:",menor)
