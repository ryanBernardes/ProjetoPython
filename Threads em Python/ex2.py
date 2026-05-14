import multiprocessing
import time
import random
#oq cada thread vai fazer
def processamento(id,valores):
    j: int = 0
    soma: int = 0
    print('Linha',id)
    print (valores)
    for j in range(5):
        soma = valores[j]+soma
        time.sleep(0.2)

    print ("Linha",id,"A soma dos valores do Vetor é:",soma)

def main():
    i: int = 0
#qtd de threads
    proc: int = 3

    params = [0]*proc
    
    #laço pra criar um vetor pra cada processo
    for i in range (proc):
        valores: int = [0]*5
        #laço pra inserir os valores no vetor
        for j in range(5):
            valores[j] = random.randint(1, 100)    
        params[i] = (i+1,valores)#define oq o vetor parametro vai receber, o valor do id e o vetor com os dados desse laço
    
    with multiprocessing.Pool(processes=proc) as pool:
        pool.starmap(processamento, params)

if __name__ == '__main__':
    main()