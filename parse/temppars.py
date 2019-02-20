from bs4 import BeautifulSoup

with open("codes.html") as fp: # html open
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
f1 = open('dict.txt', 'w') #name of file

f1.write(str(d))
f1.close()