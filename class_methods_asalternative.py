class Employee:
    no_of_leaves = 8#class variable
    def __init__(self,name,salary,role):#__init__ function serves as a constructor and helps to initialize object attributes
        self.n=name
        self.s=salary
        self.r=role
    def print_details(self):
         print(f"Employee name is {self.n} , salary is {self.s}, works as a {self.r}")
    @classmethod
    #a class method can be used to change the value of an instance variable by an object or the class itself
    def change_leaves(cls,leaves):#class method ,here cls parameter represents the class Employee itself
        cls.no_of_leaves=leaves
    @classmethod
    def from_dash(cls,string):#class method as alternative for a constructor
        #st=string.split("/")#split function takes a string as parameter and returns a 
        #list of items split on the basis of a separator like "/"
        #print(st)
        #return cls(st[0],st[1],st[2])#here we are returning the arguments of cls which is
        #the Employee class here
        return cls(*string.split("/"))
    pass

nirvik = Employee.from_dash("Nirvik/5500/Instructor")#object of the class employee
rohan = Employee("Rohan",4554,"Student")#object of the class employee

print(nirvik.s)#the salary for the object nirvik which we passed as a string is set 
print(nirvik.n)#same as above
print(nirvik.r)




