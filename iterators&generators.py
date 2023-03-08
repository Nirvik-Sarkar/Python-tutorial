"""
Iterable - __iter__() or __getitem__()#any object which has these two methods is an iterable object
Iterator - __next__()#by using the above methods we can get an iterator
Iteration -

"""

def gen(n):#iterator function
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = "Ranger"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
