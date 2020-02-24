
f = open('target.txt', "w")
f.write("hello World\n")
f.close()

f = open("target.txt")   #by default read mode
while True:
        str = f.readline()
        if str:
                print str
        else:
                break
print "----------------------------------------------"
f.seek(5)   #absolute positioning
print "Current position = ", f.tell()   #5
print f.read()    #" World\n"
f.close()
