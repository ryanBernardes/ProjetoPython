#Declaração de variáveis
n1:int  = 0  # Global
n2:int  = 0 
n3:int  = 0 
n4:int  = 0 
media:int  = 0 

def calc_media():
    global n1
    global n2
    global n3
    global n4
    global media
    media = (n1+n2+n3+n4) /4
    print ("Sua média é:",media)
    if media >= 6:
        print ("Você está aprovado")
    elif media >= 3 and media <6:
        print ("Você precisa realizar outro exame")
    elif media < 3:
            print ("Você está reprovado")

def main():
    global n1
    global n2
    global n3
    global n4
    global media
    n1 = int(input("digite a primeira nota "))
    n2 = int(input("digite a segunda nota "))
    n3 = int(input("digite a terceira nota "))
    n4 = int(input("digite a quarta nota "))
    calc_media()

if __name__ == "__main__":
    main()