#Decorator, as can be noticed by the name, is like a designer that helps to modify a function.
#The decorator can be said to be a modification to the external layer of function, as it does
#not change its structure. A decorator takes a function and inserts some new functionality in
#it without changing the function itself. A reference to a function is passed to a decorator,
#and the decorator returns a modified function. The modified functions usually contain calls
#to the original function. This is also known as metaprogramming because a part of the
#program tries to modify and add functionality to another part of the program at compile time.
def function1():
    print("Subscribe now")

func2 = function1
"""A wrapper is a function that provides a wrap-around another function. While using decorator,
all the code executed before our function that we passed as a parameter and the code after it
is executed belongs to the wrapper function. The purpose of the wrapper function is to assist
us. Like if we are dealing with a number of similar statements, the wrapper can provide us 
with some code that all the functions have in common, and we can use a decorator to call our 
function along with the wrapper. A function can be decorated many times. """
del function1
func2()#still it will generate an output because a copy of function1 has already been generated in func2()
def funcret(num):#we can return functions by a function
    if num==0:
        return print
    if num==1:
        return sum

a = funcret(1)
print(a)

def executor(func):#we can pass functions as parameters
    func("this")


executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1#decorator
def who_is_harry():
    print("Harry is a good boy")

#who_is_harry = dec1(who_is_harry)#we can write the decorator this way also

who_is_harry()

  
