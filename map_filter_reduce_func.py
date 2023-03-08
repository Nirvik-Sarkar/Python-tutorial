#---------MAP----------
l1=["34","49","63"]
l1=list(map(lambda x:int(x),l1))#this function can perform the same task on a series of iterables
l1[2]=l1[2]+2
print(l1)
def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)
#--------FILTER--------
from functools import reduce
l2=[43,26,39,52,63,79,45,22]
print(list(filter(lambda x:x%2==0,l2)))#this function can filter elements from a series of iterables
#--------REDUCE--------
l3=[1,2,3,4,5]
num=reduce(lambda a,b:a+b,l3)#Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant
print(num)