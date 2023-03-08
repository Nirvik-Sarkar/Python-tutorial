def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        c=f
        yield c
def fib(n):
    a=0
    b=1
    if (n == 1):
        yield a
    else:
        yield a
        yield b
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        yield c
n=int(input("Enter a number to find fibonacci"))
#fa=fac(n)
#for i in fa:
#    print(i)
fi=fib(n)
for i in fi:
    print(i)


    
