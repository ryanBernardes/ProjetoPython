#Declaração de variáveis
hI: int = 0
mI: int = 0
hF: int = 0
mF: int = 0
h: int = 0
m: int = 0
i: int = 0
f: int = 0

#Início
hI = int(input("digite qual foi a hora do ínicio do jogo  "))
mI = int(input("agora os minutos "))
hF = int(input("digite qual foi a hora do Final do jogo  "))
mF = int(input("agora os minutos "))

i = (hI*60)+mI
f = (hF*60)+mF
if f < i:
   f = f + 1440

duracao = f - i
h = duracao // 60
m = duracao % 60

(print("A duração do jogo foi",h,"hora(s)",m,"minuto(s)"))
#Fim
