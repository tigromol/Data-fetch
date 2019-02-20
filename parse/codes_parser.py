import os
from bs4 import BeautifulSoup
dir = os.path.dirname(__file__)

filename = os.path.join(dir, '../exchanges/ex520.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []
d = {}
for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = arrayval[x]

filename = os.path.join(dir, '../exchanges/ex520.py')
f1 = open(filename, 'w', encoding="utf-8") #name of file

f1.write(str(d))
f1.close()