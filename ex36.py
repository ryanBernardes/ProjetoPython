
s = 1  # Inicia com o primeiro termo (1/0! = 1)
f = 1
n = int(input("Digite um número para ver sua série: "))

for i in range(1, n+1):
    f = f * i        # Calcula o fatorial do termo atual
    s = s + (1 / f)  # Adiciona 1/fatorial à soma

print(s)