
# Parent Class
class Shapes:
    def __init__(self, name, side):
        self.name=name
        self.side=side

    def Area(self):
        print("I am a :" + self.name + "\n" + "i have" + self.side +"sides" )


obj_shapes=Shapes("shape", "so many")
obj_shapes.Area()

# child class 1
class Rectangle(Shapes):

    def __init__(self, len1, width2):
        self.width=len1
        self.length=width2

    def Area(self):
        result=self.length * self.width
        return result
obj_book=Rectangle(10, 7)
obj_screen=Rectangle(5,7)
print("The area of a book" + str (obj_book.Area()))
print("The area of screen" + str(obj_screen.Area()))

# child class 2
class Circle(Shapes):
    def __init__(self, pi, cirumfrance):
        self.pi=3.14
        self.cirumfrance=cirumfrance

    def Area(self):
        result=self.cirumfrance / self.pi
        return result
obj_circle=Circle(5, 10)
print("The area of a circle" + str(obj_circle.Area()))

# child class 3
class Triangle(Shapes):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def Area(self):
        result=(0.5 * self.base * self.height)
        return result
obj_tri = Triangle(5, 10)
print("The are a of Triangle"+ str(obj_tri.Area()))
