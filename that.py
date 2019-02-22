import json
import math
import sys
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numba import njit
import openpyxl as opx
from os import remove 
import scipy.stats as ss

testdata = [1,2,3,4,5]
@njit()
def amp(obser, x):
    data = []
    for i in range(x):
        for j in range(0, len(obser)-x-i, x):
            data.append(round(obser[i+j+x] - obser[i+j], 4)) # Временно снял округление
    return data
@njit()
def expgrap(obser,amps):
    data = [float(0)]
    print('expgrap')
    for i in range(int(len(obser)/2)):
        tmp = np.array(amp(obser,i))
        if(len(tmp)!=0):
            tmp1 = np.mean(tmp)
            data.append(tmp1)
    print('expgrap finished')
    return data[1:]    
@njit(nopython=True)
def dispgrap(obser,amps):
    print('dispgrap started')
    data = [float(0)]
    for i in range(int(len(obser)/2)):
        tmp = np.array(amp(obser,i))
        if(len(tmp)!=0):
            tmp1 = np.var(tmp)
            data.append(tmp1)
    return data[1:]   

def assymgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/2)):
        tmp = amp(obser,i)
        if(len(tmp)!=0):
            data.append(ss.skew(tmp))
    return data    

def excesgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/2)):
        tmp = amp(obser,i)
        if(len(tmp)!=0):
            data.append(ss.kurtosis(tmp))
    return data 

def main(args):
    font = {'size'   : 5}
    plt.subplots_adjust(wspace=2.2,hspace=2.2)
    matplotlib.rc('font', **font)
    start_time = time.time()
    amps=[1]
    #amps = [amp(args,i) for i in range(int(len(args)/2))]
    plt.figure(num=None, figsize=(10, 10), dpi=800, facecolor='w', edgecolor='k')

    plt.subplots_adjust(wspace=0.3,hspace=0.3)
    plt.subplot(5, 5, 1)
    plt.plot(args[0])
    plt.title('Original value')
    
    plt.subplot(5, 5, 2)
    plt.plot(expgrap(args[0],amps))
    plt.title('Mean value')
    
    plt.subplot(5, 5, 3)
    plt.plot(dispgrap(args[0],amps))
    plt.title('Disp value')

    plt.subplot(5, 5, 4)
    plt.plot(assymgrap(args[0],amps))
    plt.title('Assym value')
    
    plt.subplot(5, 5, 5)
    plt.plot(excesgrap(args[0],amps))
    plt.title('Kurtosis value')

    for i in range(6,16):
        
        plt.subplot(5,5,i)
        
        plt.hist(amp(args[0],i-5),bins=500,ec='black')
        plt.title(f'{i-5} minutes interval')
    for i in range(10):
        
        plt.subplot(5,5,i+16)
        
        plt.hist(amp(args[0],(i+1)*10),bins=500,ec='black')
        plt.title(f'{(i+1)*10} minutes interval')

    print(len(args))
    
    print(args[1])
    plt.savefig(f'images/{args[1]}.png')
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.clf()
if __name__ == "__main__":
    main(sys.argv[1:])

plt.show()