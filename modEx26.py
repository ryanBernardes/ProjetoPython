#Declaração de variáveis
n1:int  = 0  # Global
n2:int  = 0 
maior:int  = 0 
menor:int  = 0 


def multiplo():
    global n1
    global n2
    global maior 
    global menor
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    if maior % menor == 0:
        print(maior,"é multiplo de",menor)
    else:
        print(maior,"não é multiplo de",menor)
def main():
    global n1
    global n2
    n1 = int(input("digite o primeiro número "))
    n2 = int(input("digite o segundo número "))
    multiplo()

if __name__ == "__main__":
    main()