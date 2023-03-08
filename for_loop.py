list1 = [ ["Harry", 1], ["Larry", 2],
           ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)

for item in dict1:
     print(item)#this will only print the keys
for item, lollypop in dict1.items():#this will print all the items of the dictionary 
     print(item, "and lolly is ", lollypop)
items = [int, float, "HARRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>=6:#isnumeric() checks whether all the characters are numbers or not
        print(item)
print("Enter a no.")
# n=int(input())
# if n>6:
#   print("greater")
# for i in range(6):
#     print(i)
# for i in range(2,6):
#     print(i)
# for i in range(2,8,3):#the value of i will increment by three for each iteration
#     print(i)
for x in range(6):
  print(x)
else:
  print("Finally finished!")

