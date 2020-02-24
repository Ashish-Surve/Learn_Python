
#command line argumnets
import sys
#print ("Command line arguments = ", sys.argv)  #it is  a list




print ("--------------------------------------------")
if (len(sys.argv)==3):
    print ("Command line arguments = ", sys.argv)
    print ("File name = ", sys.argv[0])

else:
    print ("Insufficient args!!!!!")


















"""
if (len(sys.argv)==2):
    print "argv list = ",sys.argv   #is a list
    print "First argumnet fron argv list = ",sys.argv[0]  #current file name
    print "Second argument from argv list =",sys.argv[1]
    print dir(sys)
else:
    print "Insufficient arguments!!!try again!!!"



# sys.argv is a list   ['file name', , ]
"""
