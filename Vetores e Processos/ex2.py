def main():
    vetor: int = [0]*100
    maior: int = 0
    menor: int = 0
    i: int = 0
    valor: int = 0
    qtd: int = 0

    for i in range(100):
        vetor[i] = int(input("Digite um valor inteiro: "))

    maior = vetor[0]
    menor = vetor[0]
    
    for i in range(1,100):
        if(vetor[i] >maior):
            maior = vetor[i]
        elif vetor[i] < menor:
            menor = vetor[i]
    
    print ("O maior número é:",maior,"e o menor:",menor)

   
    for i in range(0,100):
        valor = vetor[i] + valor
        qtd += 1
        
        
    media = valor/qtd   
    print("A média dos valores é: ",media)


if __name__ == '__main__':
    main() 