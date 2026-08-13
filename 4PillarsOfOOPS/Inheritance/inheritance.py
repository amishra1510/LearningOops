class Animal:  #parent class
    a = 2
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Hello your name is : {self.name}")

class Humans(Animal): #child class
    pass

obj = Animal("LiON")

obj2 = Humans("Aryan")

obj2.details()
print(obj2.a) 

# child class objects has all the powers to access the attributes and methods of the parent class


##MULTI-LEVEL INHERITANCE BagFactory-->>Reebok-->>Campus
class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your bag details are : ")
        print(self.material)
        print(self.zips)
        print(self.pockets)

class Reebok(BagFactory):
    def __init__(self, material, zips, pockets,color):
        super().__init__(material, zips, pockets)
        self.color = color  

    def details(self):
        print(self.color)
        return super().details()

class Campus(Reebok):
    def __init__(self, material, zips, pockets, color,size):
        super().__init__(material, zips, pockets, color) 
        self.size = size

    def details(self):
        print(self.size)
        return super().details()

bag1 = BagFactory("Leather", 3, 4)
bag2 = Reebok("Polyester", 4, 2, "Black")
bag3 = Campus("Cotton", 3, 6, "Blue", "32L")
