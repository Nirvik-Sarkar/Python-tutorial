# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89
def harry():
    x = 22
    def rohan():
        global x
        x = 90
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)#it will be printing the value of the local variable x 

harry()
print(x)#here it will be printing the value of the global variable x





  
