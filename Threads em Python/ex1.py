import multiprocessing
import time

def processamento(id):
    time.sleep(0.5)
    print('Thread #',id)
    

def main():
    i: int = 0
    proc: int = 0

    proc = 5
    
    params = [0]*proc

    for i in range(5):
        params[i] = (i+ 1)

    with multiprocessing.Pool(processes=proc) as pool:
        # pool.map(processamento, params) #start
        pool.map(processamento, params)

if __name__ == '__main__':
    main()