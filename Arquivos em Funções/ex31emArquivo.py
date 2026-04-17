import os
n: int = 0
q: int = 0
pasta: str = 'temp'
arq: str = 'valores.txt'


def main():
    # cria diretório
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho = pasta + '/' + arq

    # abre UMA vez em modo 'w' (zera o arquivo)
    with open(caminho, 'w', encoding='utf-8') as file:
        for n in range(10, 151):
            q = n * n
            print(q)
            file.write(f"{q}\n")


if __name__ == '__main__':
    main()
