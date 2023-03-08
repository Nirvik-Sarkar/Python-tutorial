#args and kwargs in python can be used to pass huge no. of data as argument to a function
def print2(*args,**kwargs):#args receives the argument as a tuple and kwargs receives the arguments as a dictionary 
    for item in args:
        print(item)
    print("Dictionary items:")
    for x,y in kwargs.items():
        print(x,y)
mylist=["Apple","Banana","Mango","Grapes","Cherry"]
d={"Fruit":"Apple","Vegetable":"Brinjal"}
print2(*mylist,**d)