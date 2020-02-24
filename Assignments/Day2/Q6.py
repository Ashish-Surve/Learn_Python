f=open("country.txt","r")


dic={}
for l in f:
    s=l.split(",")[-1].rstrip()
    if(s in dic):
        dic[s]=dic[s]+1
    else:
        dic[s]=1

print(dic)        
