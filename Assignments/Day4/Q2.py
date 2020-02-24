class Employee:
    count=0
    def __init__(self,a="",b=0):
        self.name=a
        self.sal=b
        Employee.count+=1
    @staticmethod
    def empcount():
        return Employee.count

    def display(self):
        print("Name: ",self.name," Sal: ",self.sal)

if __name__=="__main__":
    b1=Employee("E1",9000)
    b1.display()
    b2=Employee()
    b3=Employee()
    print("Total no of E: ",Employee.empcount())
    
