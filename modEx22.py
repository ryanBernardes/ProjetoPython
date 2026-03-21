#Declaração de variáveis
n1:int  = 0  # Global
n2:int  = 0 
diferenca:int  = 0 

def diferenca():
    global n1
    global n2
    global diferenca
    if n1 > n2:
        diferenca = n1 - n2
    elif n2 > n1:
        diferenca = n2 - n1
    print("A diferença do maior para o menor é:",diferenca)

def main():
    global n1
    global n2
    n1 = int(input("digite o primeiro número "))
    n2 = int(input("digite o segundo número "))
    diferenca()

if __name__ == "__main__":
    main()