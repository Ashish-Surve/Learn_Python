import os


day=input("Which Day? ")
day.rstrip()
no=input("Number of Assignments? ")
no.rstrip()


directory=os.path.join("Day"+day)


if not os.path.exists(directory):
    os.makedirs(directory)


for  i in range(int(no)):
    open(os.path.join(directory,"Q"+str(i+1)+".py"),"w")
    
print("Assignmnets file created.... Enjoy!!!")    
