# Dunder methods (double-underscore methods)
# are special Python methods that define how objects behave
# when Python performs certain built-in operations on them.
# They are called automatically by Python when you perform the corresponding operation.

class Animal:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Hello my name is {self.name}"

obj = Animal("Lion")
obj2 = Animal("Giraffe")
print(obj)
print(obj2)

# ========================= DUNDER METHODS =========================
#
# Dunder methods = special __method__ methods that Python calls
# automatically to define how objects behave with built-in operations.
#
# Dunder = Double Underscore
#
# Method            Definition                         Called when...
# ---------------------------------------------------------------------------
# __init__()        Initializes an object               Object is created
# __str__()         User-friendly representation        print(obj) / str(obj)
# __repr__()        Developer-friendly representation   repr(obj)
# __add__()         Defines + operation                 obj1 + obj2
# __sub__()         Defines - operation                 obj1 - obj2
# __mul__()         Defines * operation                 obj1 * obj2
# __truediv__()     Defines / operation                 obj1 / obj2
# __eq__()          Defines == comparison               obj1 == obj2
# __lt__()          Defines < comparison                obj1 < obj2
# __gt__()          Defines > comparison                obj1 > obj2
# __le__()          Defines <= comparison               obj1 <= obj2
# __ge__()          Defines >= comparison               obj1 >= obj2
# __len__()         Defines object's length             len(obj)
# __getitem__()     Defines indexing behavior           obj[index]
#
# REMEMBER:
# Normal operation  →  Dunder method
# print(obj)        →  __str__()
# obj1 + obj2       →  __add__()
# obj1 == obj2      →  __eq__()
# len(obj)          →  __len__()
# obj[0]            →  __getitem__()
# ===================================================================