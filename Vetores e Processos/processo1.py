import platform
import subprocess

# Função que retorna o nome do SO
def os():
    system: str = ''
    system = platform.system()
    return system


# Função que executa o ping e lê a saída
def le_ping(processo, nome_os):
    vetor_proc: str = []
    saida = ''
    linha: str = ''

 
    vetor_proc = processo.split(' ')
    print(vetor_proc)  

    saida = subprocess.Popen(vetor_proc, stdout=subprocess.PIPE)

    linha = saida.stdout.readline().decode('utf-8', errors='ignore')

    while (linha != ''):

        if nome_os == 'Windows':
            # última linha tem "Média"
            if 'M' in linha or 'média' in linha.lower():
                vet = linha.split('=')
                if len(vet) > 1:
                    valor = vet[1].strip()
                    print('Média do ping:', valor)

        elif nome_os == 'Linux':
            # última linha tem "min/avg/max"
            if 'min/avg/max' in linha:
                vet = linha.split('=')
                if len(vet) > 1:
                    vet2 = vet[1].split('/')
                    media = vet2[1]
                    print('Média do ping:', media, 'ms')

        linha = saida.stdout.readline().decode('utf-8', errors='ignore')



def main():
    nome_os: str = ''
    processo: str = ''

    nome_os = os()

    print('Sistema Operacional:', nome_os)

    # Definindo o comando dependendo do SO
    if nome_os == 'Windows':
        processo = 'ping -4 -n 10 www.google.com.br'
    elif nome_os == 'Linux':
        processo = 'ping -4 -c 10 www.google.com.br'
    else:
        print('SO não suportado')
        return

    # Chamando a função que lê o ping
    le_ping(processo, nome_os)


if __name__ == '__main__':
    main()