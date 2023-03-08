# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y#this function is a one line version of the minus function
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))

def a_first(a):
    return a[1]
    
a =[[1, 14], [5, 6], [8,23]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])#lambda function for the a_first function which will return the 2nd element of a list
print(a)
  
