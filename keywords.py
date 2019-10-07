def doitlist(x):
    with open("strings") as f:
        k = f.read().splitlines()
    return k
def fisp(lis):
    pointlist=[]
    point=0
    chanpoint = 0
    for i in lis :
        if i==" " :
                i.replace(" ","")
                if chanpoint==0 :
                    pointlist.append(point)
                    chanpoint=chanpoint+1
        else :
            chanpoint=0
        point=point+1
    return pointlist

f = open("strings", "r")
lis = doitlist(f)
wordlist=[]
print(lis)

for i in lis:
    p = fisp(i)
    if p!=[] and p!=[0] :
        print(p)
        p=(i[p[-1]+1:])
        wordlist.append(p)
for i in lis :
   p=fisp(i)
   tmp=0
   for j in p:
     wordlist.append(i[tmp:(j)])
     tmp=j
print (wordlist)
f.close()
