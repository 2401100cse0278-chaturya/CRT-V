from math import pi
class Circle:
    def __init__(self, r):
        self.r= r

    def area(self):
        return pi * (self.r ** 2)

    def perimeter(self):
        return 2 * pi * self.r
c=Circle(5)
c1=Circle(10)
c2=Circle(15)
print(c1.area())
print(c2.perimeter())
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())