class Animal:
    a =  12 # class attribute

    def __init__(self, name):
        self.name = name  #object/instance attribute

    def hello(self):      #instance/object method (captures the location of object)
        print(f"How are you?, my name is : {self.name}")

    @classmethod  
    def details(cls):    #class method(captures the location of class so it cant use self to call attributes using self)
        print(f"How are you?, my name is : {cls.a} ")

    @staticmethod
    def speak():  # this is a static method it does not capture any location
        print("Hello, how are u I am a static method")




obj =  Animal("Lion")

print(obj.name)

obj.hello()

Animal.details()


