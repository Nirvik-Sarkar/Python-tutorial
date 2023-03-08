# f=open("Sample2.txt","w")
# f=open("Sample2.txt","a")
# c=f.write("I am having a lot of stress nowadays \n")
# print(c)#prints the no. of characters that are written in the file
f=open("Sample2.txt","r+")#in this mode we can both read and write
print(f.read())
f.write("I am suffering from mental trauma too")
f.close()