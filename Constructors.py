class Employee:
    def __init__(self,name,salary,role):#__init__ function serves as a constructor and helps to initialize object attributes
        self.h=name
        self.s=salary
        self.r=role
    def print_details(self):
         print(f"Employee name is {self.h} , salary is {self.s}, works as a {self.r}")
    pass

Nirvik=Employee("Nirvik",45000,"SWD1")#object of the class Employee
print(Nirvik.print_details())
print(Nirvik.s)
print(Nirvik.h)
Sam=Employee("Sam",35000,"SWD1")