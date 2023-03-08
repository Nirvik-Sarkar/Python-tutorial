name="Sam"
std=8
n=" My name is %s "%name#string formatting using %operator
s=" My name is %s class %d"%(name,std)#string formatting using tuple
str="I am coding in {} "
print(str.format("Python"))
str2="Hi my name is {1} {0}"#Here we are using format function
print(str2.format(name, std))
print(n)
print(s)
print(f"Hi i am {name} and i am studying in {std}th standard")#string formatting using fstring
print("Hello I am Nirvik",end=" ")#end can be used to print multiple sentences  in the same line
print("I am an IT student")
print("A;\"ranger")#can be used to print quotes single or double