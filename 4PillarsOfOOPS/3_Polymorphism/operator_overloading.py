# Operator overloading lets objects define how operators behave.
# Python uses special (dunder) methods such as __add__ for this.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2

print("Point 1:", p1)
print("Point 2:", p2)
print("Point 1 + Point 2:", p3)
