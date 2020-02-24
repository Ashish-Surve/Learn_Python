




class oPair:    # ordered pair
    
    def __init__(self, obj1, obj2):  # constructor
        self.data = (obj1, obj2)     # assign attribute , data is a tuple (6, -4)
    
    def __str__(self):              #pre defined function - we r overridding
        return str(self.data)
    
    
    __repr__ = __str__
    
    '''
    
    def __repr__(self):              #pre defined function - we r overridding
        return str(self.data)
    '''
    #-------------------------------------------------
myPair = oPair(6, -4) 	# create instance
print ("myPair = ", myPair)   #calls myPair.__str__()
#default str presenataion is  <__main__.oPair object at 0x049F2BD0>


myPair2 = oPair(10,20) 	# create instance
print ("myPair = ", myPair2)   #calls myPair2.__str__()



"""
               
    
    __repr__ = __str__

    def __repr__(self):
        return str(self.data)


        
"""












"""
def __str__(self):# str() string representation
        return str(self.data) 	        # convert tuple to string

    __repr__ = __str__ 		# repr() string representation  outside this current module

    

"""























#calls repr() when u try to print at shell>>>myPair
"""
__repr__ = __str__ 		# repr() string representation
"""
