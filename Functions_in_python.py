#there are four types of function arguments that we can provide to function
#Default arguments
#Required arguments
#Variable length arguments
#Keyword arguments
def calculate(a,b):#this are required arguments
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""#this is the doc string of this function which tells abou the function to the user or developer
    mean=(a*b)/(a+b)
    print(mean)
def greater(a,b):
    if(a>b):
        print(a,"greater than ",b)
    elif(a==b):
        print(a,"is equal to",b)
    else:
        print(b,"greater than a")
a=9
b=8
calculate(a, b)
greater(a,b)
c=5
d=4
calculate(c, d)
greater(c, d)
def average(a=5,b=7):#this are default arguments
    avg=(a+b)/2
    print(avg)
average(a,b)
average(a=9,)
#another example of default arguments
def name(fname ,mname="Jhon",lname="Whatson"):
    print("Hello",fname,mname,lname)
name("Amy",mname="Kumar")
#Keyword arguments
average(b=5,a=4)#here we can change the order of assignment of values
#Variable length arguments
def add(*number):#here we can take any number of arguments and all the arguments are taken in the form of a tuple
    sum=0
    #print(type(number))
    for i in number:#here number is a tuple
        sum=sum+i
    print(sum)
add(4,5,7,2)
#if we want to pass a dictionary as an argument to a function
def names(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James")#passing the values for the keys of the dictionary name
print(calculate.__doc__)#__doc__ prints the doc string of a function