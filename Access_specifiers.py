
# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    var = 8#this is a public class variable and can be accessed by anyone
    _protec = 9#protected variable ,this can be used by the parent class and sub classes only
    __pr = 98#private variable ,this variables can be used by the parent class only

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)#Name Mangling
"""Python does not have any strict rules when it comes to public, protected, or private, 
like java. So, to protect us from using the private attribute in any other class, Python does
name mangling, which means that every member with a double underscore will be changed to 
_object._class__variable when trying to call using an object. The purpose of this is to warn
 a user so he does not use any private class variable or function by mistake without realizing
 its states.The use of single underscore and double underscore is just a way of name mangling
because Python does not take the public, private and protected terms much seriously so we have
to use our naming conventions by putting single or double underscore to let the 
fellow programmers know which class they can access or which they can’t."""