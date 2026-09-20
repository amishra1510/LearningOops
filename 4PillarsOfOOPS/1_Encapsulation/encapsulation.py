class Factory:

    # PUBLIC CLASS ATTRIBUTE
    # Can be accessed outside the class
    name = "Kia"

    # PRIVATE CLASS ATTRIBUTE, __ means it is private
    __old = 12
    def __init__(self, color, tyre, type):
        # PUBLIC INSTANCE ATTRIBUTES
        self.color = color
        self.tyre = tyre
        self.type = type

    # PUBLIC METHOD, Can be called from outside the class
    def details(self):
        print("Color:", self.color)
        print("Tyre:", self.tyre)
        print("Type:", self.type)


    # PRIVATE METHOD, __ means it is private
    def __secret(self):
        print("This is a private method")

# CREATING AN OBJECT
obj = Factory("Black", "MRF", "Sedan")

# PUBLIC CLASS ATTRIBUTE

# We can access a public attribute using the object
print(obj.name)

# Output:
# Kia


# We can also access it using the class
print(Factory.name)

# Output:
# Kia


# We can change the public attribute
obj.name = "Maruti"

print(obj.name)

# Output:
# Maruti

# PUBLIC INSTANCE ATTRIBUTES

print(obj.color)
print(obj.tyre)
print(obj.type)

# Output:
# Black
# MRF
# Sedan

# PUBLIC METHOD, We can call a public method from outside
obj.details()
# Output:
# Black
# MRF
# Sedan

# PRIVATE ATTRIBUTE, We CANNOT directly access a private attribute
# print(obj.__old)

# This will give an error


# Python internally changes the name of __old
# because it is private.

# We can technically access it like this:
print(obj._Factory__old)

# Output:
# 12

# BUT for normal programming,
# we should NOT access it this way.

# PRIVATE METHOD

# We CANNOT normally call a private method
# obj.__secret()

# This will give an error

# INHERITANCE

class Hello(Factory):

    # Hello gets the public attributes and methods
    # from Factory
    pass


# Creating object of Hello
obj2 = Hello("White", "Apollo", "SUV")


# Public class attribute is inherited
print(obj2.name)

# Output:
# Kia


# Public method is also inherited
obj2.details()

obj2.__old  #child class cant inherit private attributes from parent class
obj2.__secret() # same for methods