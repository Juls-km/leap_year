class SingleClass:
   ...
class Person:

   pass

class Animal:
    def first_method(self):
        ...
    class Classey:
        varia = 2

        def method(self):
            print(self.varia)


    object_one=Classey()
    object_two=Classey()

    object_one.varia= 1
    object_two.varia= 5

    print(object_one.varia)
    print(object_two.varia)

class Transport:
    def __init__(self, air, water):
        self.air = air
        self.air = water

obj1_transport = Transport("Beluga","Hoverboard")
obj2 = Transport("jet", "boat")




class Person:
    def _init_(self, fname, lname):
        self.fname = fname
        self.lname = lname













class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_item(self,item_name, qty):
        item = (item_name, qty)



    def receive_item(self, item_name):
        for item in self.item:
            if item[0] == item_name:
                self.items.remove(item)

                break
       #this method computes the number of items in our cart
    def claculate_total(self):
        total = 0
        for item in self.items:
            total+=item[1]
        return total

cart= ShoppingCart()

cart.add_item(item_name ="Kiwi",qty =100 )
cart.add_item(item_name ="papaya",qty =100 )
cart.add_item(item_name ="orange",qty =100 )

print("Current Items in cart")
for item in cart.items:
    print(item[0],"-", item[1] )

total_qty=cart.calculate_total()
print("Total Quantity:",total_qty)

