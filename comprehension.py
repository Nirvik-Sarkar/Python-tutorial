"""Comprehensions in Python can be defined as the Pythonic way of writing code. Using
comprehension, we compress the code so it takes less space. Comprehension in Python converts 
the four to five lines of code into a one-liner. """
# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# ls = [i for i in range(100) if i%3==0]
#
# print(ls)


# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
dict1 = {i:f"Item {i}" for i in range(5)}
print(dict1)
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

dresses = {dress for dress in ["dress1", "dress2","dress1",
                                "dress2","dress1", "dress2"]}#set comprehension
print(dresses)

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

# for item in evens:
#     print(item)
