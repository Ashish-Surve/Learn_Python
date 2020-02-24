f=open("country.txt","r")


dic={}
for l in f:
    s=l.split(",")[-1].rstrip()
    s2=l.split(",")[0].lstrip()
    if(s in dic):
        t1=list((dic[s]))
        #print(t1,type(t1))
        t1.append(s2)
        dic[s]=t1.copy()
    else:
        dic[s]=[s2,]

print(dic)        
