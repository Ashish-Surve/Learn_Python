l=[10,20,30,40,50]
print("Original List: ",l)

l2=list(map(lambda x:x**2,l))
print("Square List: ",l2)


pairs=list(map(lambda x,y:x*y,l,l2))
print(pairs)
