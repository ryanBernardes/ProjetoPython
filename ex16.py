#Declaração de variáveis
horasT: int = 0
valorH: int = 0
perDesc: int = 0
nDep: int = 0
salBruto: int = 0
salLiquido: int = 0
salFinal: int = 0


#Início
horasT = int(input("digite as horas trabalhadas: "))
valorH = int(input("digite o valor das horas trabalhadas: "))
perDesc = int(input("digite o valor da porcentagem de desconto: "))
nDep = int(input("digite o número de dependentes: "))

salBruto = horasT*valorH
salLiquido = salBruto-((salBruto*perDesc)/100)
salFinal = salLiquido+(nDep*100)
print ("Seu Salário Bruto é :",salBruto)
print ("Seu Salário Liquído é :",salLiquido)
print ("Seu Salário Final é :",salFinal)



#Fim
