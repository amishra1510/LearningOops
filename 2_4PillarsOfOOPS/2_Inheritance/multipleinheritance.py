class Animals:
    def __init__(self,name):
        self.name = name

class Humans:
    def __init__(self,id):
        self.id = id

class Robots(Humans,Animals):
    def __init__(self, id ,name):
        Humans().__init__(id)
        Animals.__init__(name)

robo = Robots(12,"Aakash") 

#Multiple Inheritance)
#5 Multiple Inheritance means there will be 2 parent classes and
#only 1 child class and the child class will inherit all the
#attributes and methods of both parents.)
#5 Note - The constructor function in the child class will be inherited of the first
#class that has been Inherited. This is MRO(Method Resolution
#Order) followed by python.


        