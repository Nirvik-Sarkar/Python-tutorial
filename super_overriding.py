class A:
    classvar1="I am a class variable of class A"#class variable of class A
    def __init__(self):
        self.var1="I am in class A's constructor"
        self.classvar1="i am an instance variable of class A"#instance variable with same name
class B(A):
    classvar2="I am a class variable of class B"#class variable of class B
    def __init__(self):#the constructor function of the parent class has been overriden
        self.var1="I am in class B's constructor"
        self.classvar1="I am an instance variable of class B "
        super().__init__()#super function can be used to access the contents of  parent class 
        print(super().classvar1)
a=A()
b=B()        
print(b.classvar1)#when a function or variable call is made by an object of a class, the compiler 
#will search for an instance variable with the same name in the sub class and if it is not found 
#then it will search the super class for that instance variable.If the instance variable is not found 
#and there exists a class variable with the same name the class variable will be called.
  