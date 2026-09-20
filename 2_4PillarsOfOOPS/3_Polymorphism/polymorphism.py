class Animal:
    def speak(self):
        print("Animals can not speak")

class Humans:
    def speak(self):
        print("we are humans we can speak")

obj = Animal()
obj2 = Humans()

obj.speak()
obj2.speak()

#Polymorphism is a core concept in Object-Oriented Programming
#(OOP). The word means "many forms" — and in programming, it
#allows the same interface or method name to behave differently
#depending on the object or context.