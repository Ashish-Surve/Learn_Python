#10 mins break
#creating a sub class
#Exception is pre defined class, create user defined class MYError as subclass of Exception
# in java ----> class AgeError extends Exception{}

class MyError(Exception):   #inheritance
    
    pass
 
#-------------------------------------------------------------

#raise MyError("Some information about what went wrong") #object of class MyError created and then we are raising it

    

try:
    age =12
    if (age<25):
        raise MyError("Some information about what went wrong")

except MyError as error:
    print("Situation:", error)

print ("Prgrom proceeds.............")










"""
try:
    
    raise MyError("Some information about what went wrong")

except MyError as error:
    print("Situation:", error)
"""


"""

class Employee:       18    to 50  

    
class AgeError(Exception):
    pass

if (age<18 or age>50):
    raise AgeError("")
    
"""
