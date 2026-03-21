#Declaração de variáveis
n1:int  = 0  # Global
n2:int  = 0 

def maior_num():
    global n1
    global n2
    if n1 > n2:
        print (n1," É o maior número")
    elif n2 > n1:
        print (n2," É o maior número")
    else:
        print ("Os dois números são iguais")

def main():
    global n1
    global n2
    n1 = int(input("digite o primeiro número "))
    n2 = int(input("digite o segundo número "))
    maior_num()

if __name__ == "__main__":
    main()