def main():
    vetor: float = [0]*30
    i: int = 0
    valor: float = 0
    qtd: int = 0
    qtdAcima: int = 0
    posiAbaixo: int = 0
    media :float = 0

    for i in range(30):
        vetor[i] = int(input("Digite o Valor da Nota: "))

    
    for i in range(0,30):
            valor = vetor[i] + valor
            qtd += 1
    
    media = valor/qtd
    print ("A média das Notas é: ",media)

    
    for i in range(0,30):
        if vetor[i] > media:
            qtdAcima +=1

    print("A quantidade de notas acima da média é: ",qtdAcima,"\nPosição das notas abaixo da média: ")

    for i in range(0,30):
        if vetor[i] < media:
            posiAbaixo = i
            print(posiAbaixo)

    

if __name__ == '__main__':
    main() 