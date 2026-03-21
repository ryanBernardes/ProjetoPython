

def calc_velocidade(n,m,t):
    v = ((n*m)*60) / (t*1000)
    print("A velocidade média é ",v,"Km/h")
def main():
    n = int(input("digite o número de voltas: "))
    m = int(input("digite a extensão do circuito em metros: "))
    t = int(input("digite o tempo de duração em minutos: " ))

    calc_velocidade(n,m,t)

if __name__ == "__main__":
    main()