

def solve(a,left,right,value):
    ret=-1
    while(left<=right):
        mid=(left+right)//2
        if a[mid]<value:
            left=mid+1
        elif a[mid]>=value:
            ret=mid
            right=mid-1
            
    return ret        
        
        
def solveprob(A,B):
    count=0
    for i in range(len(A)):
        send=B-((A[i]*2)+A[-1])
        ret=solve(A,i,len(A)-1,send)
        if(ret!=-1):
            count+=len(A)-ret-1
            print(count)
    return count    

A=[2,3,5,8,10]
B=12

print(solveprob(A,B))
