import json
import math
import time
import numpy as np
from numba import jit   
import openpyxl as opx
from os import remove 


@jit(nopython=True)
def amp(obser, x):
   
    data = []
    for i in range(x):
        for j in range(0, len(obser)-x-i, x):
            data.append(round(obser[i+j+x] - obser[i+j], 4)) # Временно снял округление
    return data
def ampproc(obsr,x):
    data = []
    for i in range(x):
        for j in range(0, len(obser)-x-i, x):
            data.append(obser[i+j+x]/obser[i+j]-1) # Временно снял округление
    return data    
def histo(obser,amps, x, y): #This function need refactoring
    """
    х - диапазон для амплитуды
    """
    print('y: '+ str(y))
    boo = True
    while boo:
        tmp = amps
        tmp.sort()
        j = 0
        k = 0
        count = 0
        result=[]
        rang =[]
        n = int((tmp[-1] - tmp[0])) # тут 10 как и в прошлом зависит от округления
        data = [0] * y
        while k < len(data) and j<len(tmp):
            if ((tmp[j] >= (round(tmp[0]+(n/y)*k,4)))&(tmp[j] < (round(tmp[0]+(n/y)*(k+1),4)))):
                data[k] += 1                
                count += 1
                j += 1
            else:
                rang.append(round(tmp[0]+(n/y)*k,4))
                k += 1
                
        for i in range(len(data)):
            data[i] = round(data[i] / count, 4)
        boo = False
        result.append(data)
        result.append(rang)
    return result
@jit(nopython=True)
def expvalue(obser, x): 
    summ =0
    for i in obser:
        summ += i
    return summ / len(obser)


def expgrap(obser,amps):
    data = []
    print('expgrap')
    for i in range(int(len(obser)/5)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(expvalue(tmp,i))
    print('expgrap finished')
    return data    

def dispgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/5)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(disp(tmp,i))
    return data    

def assymgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/5)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(assym(tmp,i))
    return data    

def excesgrap(obser,amps):
    print('dispgrap started')
    data = []
    for i in range(int(len(obser)/5)):
        tmp = amps[i]
        if(len(tmp)!=0):
            data.append(exces(tmp,i))
    return data    

@jit(nopython=True)
def disp(obser, x):
    """
    Одно значение, дисперсия х диапазон для амплитуды и мат ожидания
    """
    summ =0
    tmp = expvalue(obser, x)
    for i in obser:  
        summ += math.pow((i - tmp),2)
      
    return summ/len(obser)

@jit(nopython=True)
def assym(obser, x):
    """
    Одно значение, ассиметрия, х диапазон для амплитуды и матожидания и дисперсии
    """
    tmp = expvalue(obser, x)
    summ=0
    size = len(obser)
    for i in obser:
        summ +=math.pow(i - tmp, 3) 
    return summ / (math.pow(math.sqrt(disp(obser, x)), 3) * len(obser))

@jit(nopython=True)   
def exces(obser, x): 
    """
    Одно значение, эксцесс, х диапазон для амплитуды и всего остального
    """
    summ = 0
    tmp = expvalue(obser, x)
    for i in obser:
        summ =math.pow(i - tmp, 4)
    return summ / (math.pow(disp(obser,x),2) * len(obser)) - 3
tmp=[]
data =[]
data2=[]
amps=[]
start = time.time()
    
    
file = open('/home/l/Documents/StatBirzhIndex/data.txt','r') #change for path

for line in file:
    data.append(line.splitlines()[0].split(','))
print(data[0])
for element in data:
    if len(element)==5:
        tmp.append(float(element[4]))
#data2.append(tmp[0:int(len(tmp)/2)])
#data2.append(tmp[int(len(tmp)/2):len(tmp)])
data2.append(tmp[0:30000])

print('Size of data = ' + str(len(data2[0])))
file.close()
print('starting amps')
startamp=time.time()

for j in range(int(len(data2[0])/5)):
    amps.append(amp(data2[0],j))

stopamp =time.time()     

print('finished amps in :' + str(startamp-stopamp))
data2.append(expgrap(data2[0],amps))
data2.append(dispgrap(data2[0],amps))
data2.append(assymgrap(data2[0],amps))
data2.append(excesgrap(data2[0],amps))

for i in range(1,int(len(amps)/2),500):
    tmp1= histo(data2[0],amps[i],1,250)
    data2.append(tmp1[0])
    data2.append(tmp1[1])
    

book = opx.Workbook()
sheet = book.active
sheet.title = "DATA"
startex=time.time()
for c in range(1, len(data2)-1):
    print('next column :' + str(c))
    print('data length :' + str(len(data2[c])))
    for r in range(2, len(data2[c]) + 2):
        _ = sheet.cell(row=r, column=c, value=data2[c-1][r-2])
print('Time for reverse parsing = '+ str(time.time()-startex))
book.save('/home/l/Documents/StatBirzhIndex/data.xlsx')  #Change for path


end = time. time()
print(end - start)