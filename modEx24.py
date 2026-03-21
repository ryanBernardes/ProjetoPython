#Declaração de variáveis
n:int  = 0  # Global


def divisivel():
    global n
    if n % 2 == 0 and n % 3 == 0 :
        print(n,"É divisível por 2 e 3")
    else:
        print(n,"Não divisível por 2 e 3")

def main():
    global n
    global n2
    n = int(input("digite o número "))

    divisivel()

if __name__ == "__main__":
    main()