def main():
    vetor: int = [0]*50
    impar: int = 0
    i: int = 0
    valor: int = 0
    qtd: int = 0

    for i in range(50):
        vetor[i] = int(input("Digite um valor inteiro: "))

    
    for i in range(50):
        if(vetor[i] >=10 and vetor[i] <=200):
            valor = vetor[i] + valor
            qtd += 1
    
    media = valor/qtd
    print ("A média dos valores entre 10 e 200 é: ",media)

    
    for i in range(50):
        if vetor[i] %2 != 0:
            impar = vetor[i] + impar
        
    print("A soma dos números ímpares é: ",impar)


if __name__ == '__main__':
    main() 