import os
from bs4 import BeautifulSoup
dir = os.path.dirname(__file__)

filename = os.path.join(dir, '../exchanges/templates/ex5.html')
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
    d[''.join(arraycont[x])] = ['5',arrayval[x]]

filename = os.path.join(dir, '../exchanges/templates/ex6.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []

for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = ['6',arrayval[x]]

filename = os.path.join(dir, '../exchanges/templates/ex8.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []

for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = ['8',arrayval[x]]

filename = os.path.join(dir, '../exchanges/templates/ex24.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []

for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = ['24',arrayval[x]]

filename = os.path.join(dir, '../exchanges/templates/ex519.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []

for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = ['519',arrayval[x]]

filename = os.path.join(dir, '../exchanges/templates/ex520.html')
with open(filename, encoding="utf-8") as fp: # html open
    soup = BeautifulSoup(fp)
array = soup.find_all('a') #list of <a>
arraycont = []
arrayval= []

for x in array:
    arraycont.append(x.contents)
    arrayval.append(x['value'])
for x in range(len(arraycont)):
    d[''.join(arraycont[x])] = ['520',arrayval[x]]

filename = os.path.join(dir, '../exchanges/codes.py')
f1 = open(filename, 'w', encoding="utf-8") #name of file
f1.write(str(d))

f1.close()