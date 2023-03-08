print("Enter a number")
n=int(input())
while(1):
    if(n<100):
        print("Enter a higher number")
        n=int(input())
        continue#when we apply the continue statement the program control re-enters the while loop and skips the below code
    elif n>=100:
        print("Congratulations you have reached 100")
        break#when the break statement is applied the control exits the loop
