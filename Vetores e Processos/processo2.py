import platform
import subprocess

def os():
    return platform.system()

def chama_processo(processo):
    vetor = processo.split(' ')
    subprocess.run(vetor)

def main():
    nome_os = os()
    opcao = 0

    while opcao != 9:
        print('1 - Listar processos')
        print('2 - Matar por PID')
        print('3 - Matar por nome')
        print('9 - Sair')

        opcao = int(input('Escolha: '))

        if opcao == 1:
            if nome_os == 'Windows':
                processo = 'TASKLIST /FO TABLE'
            elif nome_os == 'Linux':
                processo = 'ps -ef'
            else:
                print('SO não suportado')
                continue

            chama_processo(processo)

        elif opcao == 2:
            pid = input('Digite o PID: ')

            if nome_os == 'Windows':
                processo = 'TASKKILL /PID ' + pid
            elif nome_os == 'Linux':
                processo = 'kill -9 ' + pid
            else:
                print('SO não suportado')
                continue

            chama_processo(processo)

        elif opcao == 3:
            nome = input('Digite o nome do processo: ')

            if nome_os == 'Windows':
                processo = 'TASKKILL /IM ' + nome
            elif nome_os == 'Linux':
                processo = 'pkill -f ' + nome
            else:
                print('SO não suportado')
                continue

            chama_processo(processo)

        elif opcao == 9:
            print('FIM')

        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()