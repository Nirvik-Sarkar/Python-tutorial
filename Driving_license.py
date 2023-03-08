print("Enter your current age")
n=int(input())
if (n>=7 and n<=100):
    if n<18:
        print("You are not eligible to drive")
    elif n==18:
        print("We will think")
    else:
        print("You can drive")
else:
    print("Please enter a valid age")
