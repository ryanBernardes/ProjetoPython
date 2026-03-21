#Declaração de variáveis
n1:int  = 0  # Global
n2:int  = 0 
n3:int  = 0 
n4:int  = 0 

def ordem_cresc():
    global n1
    global n2
    global n3
    global n4
    if n4 <= n1:
        print(n4,",",n1,",",n2,",",n3)
    elif n4 <= n2:
        print(n1,",",n4,",",n2,",",n3)
    elif n4 <= n3:
        print(n1,",",n2,",",n4,",",n3)
    else:
        print(n1,",",n2,",",n3,",",n4)


def main():
    global n1
    global n2
    global n3
    global n4
    n1 = int(input("digite o primeiro número "))
    n2 = int(input("digite o segundo número "))
    n3 = int(input("digite o terceiro número "))
    n4 = int(input("digite o quarto número "))

    ordem_cresc()

if __name__ == "__main__":
    main()