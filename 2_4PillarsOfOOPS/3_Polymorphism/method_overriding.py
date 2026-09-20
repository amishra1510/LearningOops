# Method overriding lets a child class provide its own implementation
# of a method already defined in the parent class.


class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
