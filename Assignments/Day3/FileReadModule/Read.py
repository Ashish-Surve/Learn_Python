
def ReadfromFile(path="country.txt"):
    try:
        f=open(path,"r")
    except(FileNotFoundError):
        raise FileNotFoundError()
    except(Exception):
        raise Exception()
    
    dic={}
    for l in f:
        sSplit=l.split(",")
        s=sSplit[-1].rstrip()#language
        s2=sSplit[0].lstrip()#country
        s3=sSplit[2].rstrip()#State
        if(s in dic):
            t1=dict((dic[s]))
            #print(t1,type(t1))
            t1[s2]=[s3,]
            dic[s]=t1.copy()
        else:
            dic[s]={s2:[s3,]}
    return dic        


if(__name__=="__main__"):        
    print(ReadfromFile())
