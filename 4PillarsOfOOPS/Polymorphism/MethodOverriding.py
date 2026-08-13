class Animal:
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Your name is : {self.name}")

class Humans(Animal):
    b = 12
    def __init__(self, name):
        super().__init__(name)

    def details(self):
        super().details()   ## this needs to be added or else the parent class method can never be accessed 
        print(f"Your info is {self.name} and this is all we have")


obj = Humans("Harsh")

print(obj.a)
print(obj.b)
obj.details()
   #both the methods are called by the object but, only the method from the child class 
                #will be observed as output 
                #this is known as Method Overriding.


#when we are doing inheritance and parent and child classes have same 
#method names then the child class method will override the parent class method
