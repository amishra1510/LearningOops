class Animal:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Hello my name is {self.name}"

obj = Animal("Lion")

print(obj)