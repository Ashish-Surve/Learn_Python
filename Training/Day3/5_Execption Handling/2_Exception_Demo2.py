#try statement with multiple excepts
def safe_float(object):
    try:
        #print(num1)
        retval = float(object)    #this is pre-defined fuction - float()
    
    except ValueError as a :
        retval = 'could not convert non-number to float = ',a
    except TypeError as a :
        retval = 'object type cannot be converted to float = ',a
    except Exception as a :
        retval = 'Generic '
    return retval

ret1=safe_float(3)      #call successful
print  ("o/p of safe_float(3) = ", ret1)

print ("--------------------------------------------")
ret2=safe_float('abc')   #ValueError
print ("ret2 = ",ret2)

print ("--------------------------------------------")
ret3 = safe_float({'a': 'Dict'})  #TypeError
print ("ret3 = ",ret3)
print ("--------------------------------------------")
