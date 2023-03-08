print("Enter the Year")
y=int(input())
if y%100==0:
    if(y%400==0):
        print(y," Is a Leap year")
    else:
        print(y," Is not a Leap year")
elif y%4==0:
    print(y, "Is a Leap year")
else:
    print(y,"Is not a Leap year")
