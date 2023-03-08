print("Enter a no. less than 10")
n=int(input())
print("0 or 1")
c=int(input())
b=bool(c)
k=n
if b==True:
    for i in range(0,n):
        print("\n")
        for j in range(0,i+1):
            print("* ",end=" ")
else:
    for i in range(n,0,-1):
        print("\n")
        for j in range(0,i):
                        print("* ",end=" ")

            
