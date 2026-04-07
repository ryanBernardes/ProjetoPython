import os

# globais
n: int = 0
maior: int = 0
menor: int = 0

dir: str = '/tmp/exercicios'
arq: str = 'ex38.txt'

def main():
    global n, maior, menor

    # cria diretório
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chmod(dir, 0o744)

    n = int(input("Digite o 1º número: "))
    maior = n
    menor = n

    escreveArq(dir, arq, str(n) + '\n')

    for i in range(2, 11):
        n = int(input())

        if n > maior:
            maior = n

        if n < menor:
            menor = n

        escreveArq(dir, arq, str(n) + '\n')

    escreveArq(dir, arq, "Maior: " + str(maior) + '\n')
    escreveArq(dir, arq, "Menor: " + str(menor) + '\n')

    print("O maior número foi:", maior, "e o menor:", menor)

def escreveArq(dir, arq, linha_arq):
    tipo: str = ''
    enc: str = 'utf-8'

    caminho = dir + '/' + arq

    if os.path.exists(dir) and os.path.isdir(dir):

        if os.path.exists(caminho):
            tipo = 'a'
        else:
            tipo = 'w'

        with open(caminho, tipo, encoding=enc) as file:
            file.write(linha_arq)
    else:
        print("Diretório inválido")

if __name__ == '__main__':
    main()
