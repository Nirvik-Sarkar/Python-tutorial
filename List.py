numbers=[12,8,17,9,6,5,2]
numbers.sort()#sorts an unsorted list and has a permanent effect on the main list
numbers.reverse()#reverses the list and has a permanent effect on the main list
numbers.append(13)
numbers.insert(2,-3)#inserts a new element at a particular index of the list
numbers.append(-5)#inserts a new element at the end of a list
numbers.pop()#removes the last element
numbers.remove(2)#in order to remove a particular element from a list
print(numbers)
#print(len(numbers))#prints the lenth of a given list
#print(max(numbers))#prints the maximum number from a given list ands acts opposite to the minimum number
#print(numbers[1:5])
#print(numbers[:8])
#print(numbers[0:])
#print(numbers[1:-2])
#print(numbers[1:8:2])#prints the elements of list within a specified index and jumping over elements as mentioned
#print(numbers[1:8:-2])#taking negative numbers for jumping is not advisable as it doesn't give the desired output
print(numbers[::-2])#negative numbers only work when we take the default values
#Mutable-values can be changed just like a list
#Immutable -values can't be changed just like a tuple
tp=(1,2,3)
#tp[2]=8#will give error as tuple object can't be changed
#del tp#this will delete the tuple tp
print(tp)
mylist=list(tp)#converting a tuple to list in order to change its values
mylist[0]=5
tp=tuple(mylist)
print(tp)
print(len(tp))

