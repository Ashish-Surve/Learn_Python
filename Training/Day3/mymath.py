pi=3.141592653589
def area(r):
    global pi
    return (pi*r**2)

def fib(n):
    a,b=0,1
    while(b<n):
        print(b)
        a,b=b,a+b
    
print("="*50)
if __name__=="__main__":
    fib(21)
    print(area(5))
print("="*50)
