import multiprocessing
import time
import random
#oq cada thread vai fazer
def processamento(id):
    distPer: int = 0
    distanciaMax: int = 15
    saltoMax = random.randint(1,5)

    while distPer < distanciaMax:
        salto = random.randint(0, saltoMax)
        distPer += salto
        if distPer < distanciaMax:
            print("Sapo",id,"pulou",salto,"cm","Percorreu",distPer,"cm")
        elif distPer >= distanciaMax:
            print('Sapo',id,"Chegou")
        time.sleep(0.1)
        


def main():
    i: int = 0
#qtd de threads
    proc: int = 5

    params = [0]*proc
    
    #laço pra criar um id pra cada processo
    for i in range (proc):  
        params[i] = (i+1)#define oq o vetor parametro vai receber, o valor do id e o vetor com os dados desse laço
    
    with multiprocessing.Pool(processes=proc) as pool:
        pool.map(processamento, params)

if __name__ == '__main__':
    main()