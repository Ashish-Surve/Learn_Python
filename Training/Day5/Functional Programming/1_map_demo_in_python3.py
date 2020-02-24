

nums = [1,2,3]
squareelemnts = [i**2 for i in nums if i<3]  #list comprehension
print("Original nums list = ", nums)
print("List of square elemnts = ", squareelemnts) #[1, 4]

def sq_elem(x):
    return x**2
squareelemnts2 = [sq_elem(i)for i in nums]
print("List of square elemnts = ", squareelemnts2)#[1, 4, 9]
print("sq_elem(5) = ", sq_elem(5))

#2)alternative solution in map() function call:
map_obj = map(sq_elem, nums)  #sq_elem is a func   functional programming
print("map_obj = ", map_obj)  #<map object at 0x0410AE30> 1,4,9
newlist1 = list(map_obj)
print("List of square elemnts = ",newlist1)
print ("---------------------------------------------------")

print("Output of map with lambda = ",list(map(lambda x : x**2,nums)))
print("filter and map = ",list(map(lambda x : x**2,list(filter(lambda x: x<3,nums)))))


print ("---------------------------------------------------")
#in python 3
words =["abc", "xyz", "lmn"]
upper_words = []
map_ob = map(lambda w :w.upper() , words)
print( "Return value of map in Python 3 = ", map_ob)
upper_words = list(map_ob)
print ("Original sequence list = ", words)
print("Upper words = ", upper_words)


#in Python3 map() function returns map object so pass that as parameter to list
