class Shapes():
    def __init__(self, name, area):
        self.name = name
        self.area = area
   
class Circle(Shapes):
    def area(self):
        return self.radius * self.radius * 3.14

    def __init__(self, radius):
        self.radius =radius

class Rectangle(Shapes):
    def __init__(self, longSide, shortSide):
        self.longSide = longSide
        self.shortSide = shortSide

    def area(self):
        return self.longSide * self.shortSide

class Square(Shapes):
    def __init__(self, widthSide, heightSide):
        self.widthSide = widthSide
        self.heightSide = heightSide

    def area(self):
        return self.widthSide * self.heightSide 

class Ellipse(Shapes):
    def area(self):
        return self.radius *self.radius * 3.14

    def __init__(self, radius):
        self.radius = radius

circle1 = Circle(10)
print("Circle 1 area: ", circle1.area())

r1 = Rectangle(7, 8)
r2 = Rectangle(1, 3)
print("Rectangle 1 area: ", r1.area())
print("Rectangle 2 area: ", r2.area())

square1 = Square(10,10)
print("Square 1 area: ", square1.area())

ellipse1 = Ellipse(8)
print("Ellipse 1 area: ", ellipse1.area())


               
