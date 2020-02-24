#class defination: OOP
class SayHello:                             #Class defination
    greeting1 ="BYE!!!!"        #NOT a instance var
    def __init__(self1):                     #constructor Function, catching argumnet name self can anything else also
        """init constructor function"""
        print ("In init constructor function , self = ", self1)
        self1.greeting = "Hello Everyone!!!Hope enjoying Python Session........."
    def display(self):
        print ("In display greeting = ", self.greeting)

    @classmethod
    def getmsg(cls):
        return cls.greeting1
        
#---------------------------------------------------------------------------------
obj1 = SayHello()                          #calling __init__() constructor function
print ("In main program , obj1 = ", obj1)
print ("Greeting = ",obj1.greeting)
obj1.display()                              #over this function call obj1 itself is passed as default first argument
print ("-------------------------------------------------------------------------")

obj2 = SayHello()
print ("In main program , obj2 = ", obj2)
print ("Greeting = ",obj2.greeting)
obj2.display()  
#print ("Obj1 greeting 1=", obj1.greeting1) #Not suggested
print ("Obj1 greeting 1=", SayHello.greeting1) #suggested

print("SayHello.getmsg() = ", SayHello.getmsg())









