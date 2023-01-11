import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circu(self):
        return 2*math.pi* self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)

    # getter setter
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        if value <= 0:
            raise TypeError("must be positive number")
        self.__radius = value

circle = Circle(10)
print("Circu:", circle.get_circu())
print("Area:", circle.get_area())
# print("Radius:", circle.__radius)

#
print(circle.get_radius())

circle.set_radius(2)
print("Circu:", circle.get_circu())
print("Area:", circle.get_area())

#
#@property
#def radius(self):
#    return self.__radius
#@radius.setter
#def radius(self, value):
#    if value <= 0:
#        raise TypeError("must be positive number")
#    self.__radius = value

#circle.radius = 2