import json
import math
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from numba import jit   
import openpyxl as opx
from os import remove 
import scipy.stats as ss

testdata = [1,2,3,4,5]
@jit(nopython=True)
def amp(obser, x):
    data = []
    for i in range(x):
        for j in range(0, len(obser)-x-i, x):
            data.append(round(obser[i+j+x] - obser[i+j], 4)) # Временно снял округление
    return data
@jit(nopython=True)
def expgrap(obser,amps):
    data = [float(0)]
    print('expgrap')
    for i in range(int(len(obser)/2)):
        tmp = np.array(amp(obser,i))
        if(len(tmp)!=0):
            tmp1 = np.mean(tmp)
            data.append(tmp1)
    print('expgrap finished')
    return data    
@jit(nopython=True)
def dispgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/2)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(np.val(tmp))
    return data    
@jit(nopython=True)
def assymgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/2)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(ss.skew(tmp))
    return data    
@jit(nopython=True)
def excesgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/2)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(ss.kurtosis(tmp))
    return data    

def main(args):
    start_time = time.time()
    amps=[1]
    #amps = [amp(args,i) for i in range(int(len(args)/2))]
    plt.plot(expgrap(args,amps))
    print(len(args))
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()
if __name__ == "__main__":
    main(sys.argv[1:])

plt.show()