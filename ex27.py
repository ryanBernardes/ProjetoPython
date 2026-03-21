#Declaração de variáveis
n: int = 0
m: int = 0
t: int = 0
v: int = 0



#Início
n = int(input("digite o número de voltas: "))
m = int(input("digite a extensão do circuito em metros: "))
t = int(input("digite o tempo de duração em minutos: " ))

v = ((n*m)*60) / (t*1000)
print("A velocidade média é ",v,"Km/h")



#Fim