"""Operator Overloading means giving extended meaning beyond their predefined operational meaning.
 For example operator + is used to add two integers as well as join two strings and merge two list
 s. It is achievable because ‘+’ operator is overloaded by int class and str class. """
 
"""Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) 
 represent dunder methods."""
 
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):#this is a dunder method used to override the '+' operator
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):#__repr__() function returns the object representation in string format.
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):#This method returns the string representation of the object(same as __repr__). 
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))#way to ipmplement dunder methods
print(emp1 + emp2)
"""Difference between __str__ and __repr__ functions
If the implementation of __str__ is missing, then __repr__ function is used as a fallback. 
If the implementation of __repr__ is missing, then there will be no fallback.
If __repr__ function is returning the object's String representation, we can skip the 
implementation of __str__ function. 
The priority of __str__ is higher than __repr__."""