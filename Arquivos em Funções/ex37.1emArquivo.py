import os

pasta = 'temp'
arquivo = 'fibonacci.txt'


def escreve_termo(caminho, valor, primeiro=False):
    modo = 'w' if primeiro else 'a'

    with open(caminho, modo, encoding='utf-8') as f:
        f.write(f"{valor}\n")


def main():
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = pasta + '/' + arquivo

    n = int(input("Digite n: "))  

    a, b = 0, 1

    for i in range(1, n + 1):
        print(a)

        escreve_termo(caminho, a, i == 1)

        c = a + b
        a = b
        b = c


if __name__ == '__main__':
    main()
