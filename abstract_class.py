# from abc import ABCMeta,abstractmethod #this is a necessary module that needs to be imported 
#to create an abstract base class
from abc import ABCMeta, abstractmethod#this is a decorator present in abc module used to declare
#abstract methods
class Shape(metaclass=ABCMeta):#A helper class that has ABCMeta as its metaclass. With this class, an 
#abstract base class can be created by simply deriving from ABC
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())