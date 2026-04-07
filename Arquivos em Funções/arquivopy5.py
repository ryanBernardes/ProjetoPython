import os

dir: str = '/tmp/exercicios'
arq: str = 'ex36.txt'

def main():
    s: float = 1
    n = int(input("Digite um número: "))

    # cria diretório
    if not os.path.exists(dir):
        os.makedirs(dir)
    os.chmod(dir, 0o744)

    # grava primeiro termo
    escreveArq(dir, arq, "1/0! = 1\n")

    for i in range(1, n+1):
        fat = fatorial(i)
        termo = divisao(1, fat)
        s += termo

        linha = "1/" + str(i) + "! = " + str(termo) + "\n"
        escreveArq(dir, arq, linha)

    escreveArq(dir, arq, "Resultado: " + str(s) + "\n")

    print("Resultado:", s)

def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def divisao(a, b):
    return a / b

def escreveArq(dir, arq, linha):
    caminho = dir + '/' + arq

    if os.path.exists(caminho):
        tipo = 'a'
    else:
        tipo = 'w'

    with open(caminho, tipo) as f:
        f.write(linha)

if __name__ == '__main__':
    main()
