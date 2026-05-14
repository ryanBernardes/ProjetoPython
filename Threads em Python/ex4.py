import platform
import subprocess
import multiprocessing


# função para descobrir o sistema operacional
def os():

    sistema = platform.system()

    return sistema


# função que executa e lê o ping
def le_ping(processo, nome_servidor, nome_os):

    vetor_proc = []
    saida = ''
    linha = ''

    # separa o comando em vetor
    vetor_proc = processo.split(' ')

    # executa o comando
    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)

    # lê a primeira linha
    linha = saida.stdout.readline().decode('utf-8', errors='ignore')

    # continua lendo enquanto houver linha
    while linha != '':

        # WINDOWS
        if nome_os == 'Windows':

            # imprime cada iteração
            if 'tempo=' in linha.lower():

                vet = linha.split('tempo=')

                if len(vet) > 1:

                    tempo = vet[1].strip()

                    print(nome_servidor, '->', tempo)

            # pega média final
            if 'média' in linha.lower():

                vet = linha.split('=')

                if len(vet) > 1:

                    media = vet[1].strip()

                    print(nome_servidor, '-> Média:', media)

        # LINUX
        elif nome_os == 'Linux':

            # imprime cada iteração
            if 'time=' in linha.lower():

                vet = linha.split('time=')

                if len(vet) > 1:

                    tempo = vet[1].split(' ')[0]

                    print(nome_servidor, '->', tempo, 'ms')

            # pega média final
            if 'min/avg/max' in linha:

                vet = linha.split('=')

                if len(vet) > 1:

                    vet2 = vet[1].split('/')

                    media = vet2[1]

                    print(nome_servidor, '-> Média:', media, 'ms')

        # lê próxima linha
        linha = saida.stdout.readline().decode('utf-8', errors='ignore')


# função executada pelos processos
def processamento(dados):

    nome_servidor = dados[0]

    endereco = dados[1]

    nome_os = ''

    processo = ''

    nome_os = os()

    print('Servidor:', nome_servidor)
    print('Sistema Operacional:', nome_os)

    # monta comando correto
    if nome_os == 'Windows':

        processo = 'ping -4 -n 10 ' + endereco

    elif nome_os == 'Linux':

        processo = 'ping -4 -c 10 ' + endereco

    else:

        print('SO não suportado')

        return

    # executa leitura do ping
    le_ping(processo, nome_servidor, nome_os)


def main():

    proc = 3

    # lista de parâmetros
    servidores = [0] * proc

    # (nome fixo, endereço)
    servidores[0] = ('UOL', 'www.uol.com.br')

    servidores[1] = ('Terra', 'www.terra.com.br')

    servidores[2] = ('Google', 'www.google.com.br')

    # cria os processos
    with multiprocessing.Pool(processes=proc) as pool:

        pool.map(processamento, servidores)


if __name__ == '__main__':

    main()