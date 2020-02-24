#write to file
f = open("myfile1.txt", "w")             #file  object created in write mode
print dir(f) #list of all attributes and functions of passed object
print "-------------------------------------------------------------------"
f.write("Welcome to PSL\t\t Pune \n 2018")
f.write("Python programming\n")
f.write("Session in Progress!!!\n")
f.write ("""abc
            xyz""")
f.close()

#read from a file
f1 = open ("myfile.txt")  #this file should be existing to read
print "1 line = ", f1.readline()   #f1 object is at the EOL
print "2 line = ", f1.readline()
print f1.read()
f1.close()

#assignment
#read content from source.txt and copy it in target.txt









"""
#f = open("c:\\data\\myfile.txt", "a")             #file  object created in write mode
#f = open(r"c:\data\myfile.txt", "a")             #file  object created in write mode

f1 = open ("myfile.txt")  #this file should be existing to read
print "1 line = ", f1.readline()   #f1 object is at the EOL
print "2 line = ", f1.readline()


f1.close()

"""







#print "Current file position = ", f1.tell()
#print "Line after seek = ", f1.readline()

#print "1 line = ", f1.readline()
#print "Whole content in a list  =\n", f1.readlines()
#print "Whole content as text = \n", f1.read()   #read the whole content
#print "Read = ",f1.read(1)


#print "----------------------------------------------------------------------------------"
#str = "Hello"
#print dir (str)























"""

print "-------------------------------------------------------------------"
str = "Hello"
print dir(str)
print "-------------------------------------------------------------------"
l1=[1,2,3]
print dir(l1)
print "-------------------------------------------------------------------"
"""
