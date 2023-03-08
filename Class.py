class Employee:
    no_of_leaves = 8#class variable
    @classmethod
    #a class method can be used to change the value of an instance variable by an object or the class itself
    def change_leaves(cls,leaves):#class method ,here cls parameter represents the class Employee itself
        cls.no_of_leaves=leaves
    pass

nirvik = Employee()#object of the class employee
rohan = Employee()#object of the class employee

nirvik.name = "Nirvik"#instance variable of the object nirvik
nirvik.salary = 455
nirvik.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

# print(Employee.no_of_leaves)
# print(Employee.__dict__)#__dict__ is an attribute which returns a dictionary comprising of all the instance variables of an object or class
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)
# print(nirvik.__dict__)
nirvik.change_leaves(54)
print(nirvik.no_of_leaves)

