#Declaração de variáveis
tempo: int = 0
velocidade: int = 0
lGasto: int = 0


#Início
tempo = int(input("digite o tempo de percurso: "))
velocidade = int(input("digite a velocidade média: "))


lGasto = (tempo*velocidade)/12

print ("A quantidade em litros de gasolina gasta será de :",lGasto)



#Fim
