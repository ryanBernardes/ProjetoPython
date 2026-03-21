base = int(input("Digite o valor da base: "))
expo = int(input("Digite o valor do expoente: "))
valor = 1
for i in range(1,expo+1):
    valor = valor*base

print(valor)

