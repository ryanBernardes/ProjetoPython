import os

valor: int = 0
dir: str = '/tmp/exercicios'
arq: str = 'ex34.txt'

def main():
    global valor

    contador = 1

    if not os.path.exists(dir):
        os.makedirs(dir)

    os.chmod(dir, 0o744)

    valor = int(input("Digite um valor entre 1 e 10: "))

    while contador <= 10:
        result = mult(valor, contador)
        grava(contador, result)
        contador += 1

def mult(vlr, tab):
    return vlr * tab

def grava(c, rslt):
    global dir, arq

    caminho = dir + '/' + arq
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):

        if c == 1:
            tipo = 'w'
        else:
            tipo = 'a'

        with open(caminho, tipo, encoding='utf-8') as file:
            file.write(linha)
    else:
        print("Diretório inválido")

if __name__ == '__main__':
    main()