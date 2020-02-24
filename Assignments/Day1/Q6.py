print("Enter elements?")
x=""
l=[]
while(1):
    x=input("Enter no: ")
    if( not x.isnumeric()):
        break
    else:
        l.append(int(x))
l.sort()    
print(l)    



