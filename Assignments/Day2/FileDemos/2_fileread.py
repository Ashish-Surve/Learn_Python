
myfile = open('data.txt', "r")  #csv
f = open("target.txt", "w") 
while True:
        str = myfile.readline()
        if str:
                print str
                f.write(str)
        else:
                print "Nothing in file"
                break
myfile.close()
f.close()
print myfile
print myfile.tell()   #error  ValueError
print "END!!!!!"
"""
for i in f:
        print i
"""
