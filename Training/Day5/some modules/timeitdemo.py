

#performance measure
from timeit import Timer  #class Timer
t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print ("t1 =", t1) #0.05611799134514599

t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()#0.03536866522034211
print ("t2 =", t2 )
#0.54962537085770791
