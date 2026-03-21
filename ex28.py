#Declaração de variáveis
precoAtual: float = 0
mediaMensal: float = 0
novoPreco: float = 0



#Início
precoAtual = float(input("digite o preço atual "))
mediaMensal = float(input("digite a média mensal "))


if mediaMensal < 500 and precoAtual < 30:
    novoPreco = precoAtual * 1.10
elif mediaMensal >= 500 and mediaMensal < 1000 and precoAtual >= 30 and precoAtual < 80 :
    novoPreco = precoAtual * 1.15
elif mediaMensal >= 1000 and precoAtual >= 80:
    novoPreco = precoAtual * 0.95
else:
    novoPreco = precoAtual

print("O novo preço será ",novoPreco,"R$")





#Fim
