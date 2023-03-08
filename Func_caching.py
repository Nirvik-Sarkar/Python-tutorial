#Function caching is a way to improve code's performance by storing the function's return values.
import time
from functools import lru_cache

@lru_cache(maxsize=32)#this is a decorator from functools which can be used to store function call
#data in cache memory,it takes maxsize as parameter  to save the number of function call values
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")

