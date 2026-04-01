import os

# globais
nome: str = ''
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
valor_media: float = 0

dir: str = '/tmp/exercicios'
arq: str = 'ex21.txt'

def main():
    contador: int = 0

    # cria diretório e permissão
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chmod(dir, 0o744)

    # chama 5 vezes entrada
    while contador < 5:
        entrada()
        contador += 1

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media

    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))

    valor_media = med(nota1, nota2, nota3, nota4)

    print("Média:", valor_media)

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def med(n1, n2, n3, n4):
    media: float = (n1 + n2 + n3 + n4) / 4
    return media

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq

    linha = nm + ";" + str(nt1) + ";" + str(nt2) + ";" + str(nt3) + ";" + str(nt4) + ";" + str(vlr_med) + "\n"

    escreveArq(dir, arq, linha)

def escreveArq(dir, arq, linha_arq):
    file: str = ''
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