
class Circle:
    def __init__(self,r=0):
        self.radius=r

    def area(self):
        return (self.radius**2*3.1415926535897931)


c1=Circle(5)
c2=Circle(6)
c3=Circle(7)

print("C1 Area: ",c1.area())
print("C2 Area: ",c2.area())
print("C3 Area: ",c3.area())
        
