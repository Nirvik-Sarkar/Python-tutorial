s = set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)#a set can be easily implemented using a list
print(s_from_list)
#print(type(s_from_list))
s.add(1)#to add elements in a list
s.add(2)
s.remove(2)#to remove elements from a list
s1 = {4, 6}
print(s.isdisjoint(s1))
s2=s1.union({1,2,3})#forms a new set s2 as union of the specified elements and elements of S1
s3=s1.intersection({1,2,4})#forms a new set s3 comprisingof all the common elements from the specified elements and elements of S1
print(s2)
print(s3)

