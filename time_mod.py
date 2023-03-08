import time
init=time.time()#it returns time in ticks
print(init)
k=0
while(k<5):
    print("Ranger7652")
    k+=1
    time.sleep(2)#it can be used to stop the program for few seconds
print("while loop ran in",time.time()-init)
init2=time.time()
for i in range (5):
    print("Ranger7652")
print("For loop ran in",time.time()-init2)
#time.localtime() converts the ticks in local time and returns a tuple 
#in order to represent the tuple in a presentable format we use the time.asctime()
local=time.asctime(time.localtime((time.time())))
print(local)

    
