def calculate(a,b):#this are required arguments
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""#this is the doc string of this function which tells abou the function to the user or developer
    mean=(a*b)/(a+b)
    print(mean)
print(__name__)#name of the current module here is main
if __name__=='__main__':#this is done to ensure that when the module will be called only the useful function will get executed
    c=calculate(a=9, b=4)
    print(c)
