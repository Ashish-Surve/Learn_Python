emp={'1a':30000,'2a':40000}

str1=input("ID [space] Salary :")

str1=str1.split(" ")

emp[str1[0]]=int(str1[1])

t=list(emp.keys())
t.sort()
#print(t)
for x in t:
    print("ID :",x," Salary :",emp[x])

emp={x:emp[x]+5000 for x in emp.keys()}

print(emp)

