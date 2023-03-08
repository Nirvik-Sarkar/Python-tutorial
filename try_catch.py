print("Enter the 1st no.")
n1=input()
print("Enter the 2nd no.")
n2=input()
try:
    print("Sum of the 2 numbers is",int(n1) + int(n2))
except Exception as e:
    print(e)
print("IMPORTANT")
