from abc import ABC, abstractmethod

class Animal(ABC): #Abstract class

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat says meow!")

# Abstraction means hiding the implementation details and showing only what is necessary.
# Animal is an abstract class, so we cannot create its object directly.
# It defines a method as a rule that every child class must follow.
# Child Class provide their own implementation of Parent Class.
# @abstractmethod forces the child classes to implement that method.