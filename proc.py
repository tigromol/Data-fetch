from PIL import Image
import math
data = []
datadate = []
datatime = []
indexes=[0] #here is indexes
fulldata=[0]*10400000 #pins 
def f7(seq):  #duplicate proof
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
def inminutes(seq): #date to number of minutes
    return (int(seq[0])-2000)*525600 + int(seq[1])*43800 + int(seq[2])*1440
def inminutesT(seq): #time to number of minutes
    return (int(seq[0])*60) + int(seq[1])
def listtoimg(seq):
    num = len(seq)

    data = [(255, 255, 255) if pixel == 1 else (0, 0, 0) for pixel in seq]
    img = Image.new('RGB', (1440,math.ceil(num/1440)), "white") 
    img.putdata(data)
    img.show()             
    img.save('Image2.png')
for count in range(18): #unite all the files
    f = open('%d.txt' % (count+3),'r')
    for line in f:
        data.append(line)
    f.close()
datafiltered = f7(data) #remove duplitcates
filewr = open('D&J_2001_2019','w') #open file for writing
data = [x.split(',') for x in data] #each line in arr
for x in data: # collect dates array
    datadate.append([x[2][:4],x[2][4:6],x[2][6:]])
for x in datadate: #normalize
    indexes.append(inminutes(x)-indexes[0])
datadate=[]
for x in data: #collect times array 
    datatime.append([x[3][:2],x[3][2:4],x[3][4:]])

for x in range(len(datatime)): #normalize time
    indexes[x] = indexes[x]+inminutesT(datatime[x])
datatime=[]
for x in indexes:
    fulldata[x]=1
listtoimg(fulldata)
for elem in indexes:
    filewr.write(str(elem))
print(str(len(data)/9460800))
filewr.close()            