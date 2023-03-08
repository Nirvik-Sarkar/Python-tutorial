
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9#it is ovrriding the value of basketball which it has inherited from the 
    #class Dad
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):#first it will find for any variable or function within itself only then 
#if it is not found ,it will search for them in the class which it has inherited from
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)

# electronic device
# pocket gadget
# phone



