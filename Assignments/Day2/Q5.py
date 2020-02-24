f=open("empdata.txt")
dic={}
p=f.readlines();
for l in p:
    l=l.split(":")
    dic[l[0]]={"Name":l[1],"Age":int(l[2]),"Salary":int(l[3])}

print(dic)
