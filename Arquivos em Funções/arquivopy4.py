import os

dir: str = '/tmp/exercicios'
arq_entrada: str = 'ex38.txt'
arq_saida: str = 'multiplos5.txt'

def main():
    caminho_entrada = dir + '/' + arq_entrada

    if os.path.exists(caminho_entrada):

        with open(caminho_entrada, 'r') as file:
            for linha in file:

                linha = linha.strip()

                # ignora "Maior" e "Menor"
                if 'Maior' in linha or 'Menor' in linha:
                    continue

                # converte para inteiro
                numero = int(linha)

                # verifica múltiplo de 5
                if numero % 5 == 0:
                    escreveArq(dir, arq_saida, str(numero) + '\n')
    else:
        print("Arquivo não encontrado")

def escreveArq(dir, arq, linha_arq):
    tipo: str = ''
    caminho = dir + '/' + arq

    if os.path.exists(dir) and os.path.isdir(dir):

        if os.path.exists(caminho):
            tipo = 'a'
        else:
            tipo = 'w'

        with open(caminho, tipo) as file:
            file.write(linha_arq)
    else:
        print("Diretório inválido")

if __name__ == '__main__':
    main()
