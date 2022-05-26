import math

class Cone:
    def __init__(self, radius, height, hypotenuse):
        self._radius = radius
        self._height = height
        self._hypotenuse = hypotenuse

    def get_volume(self) -> float:
        return (1/3)*math.pi*self._radius*self._radius*self._height

    def get_area(self) -> float:
        return (math.pi*self._radius*self._radius)+(math.pi*self._radius*self._hypotenuse)

class Parallelepiped:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_volume(self) -> float:
        return self._x*self._y*self._z

    def get_area(self) -> float:
        return (self._x*self._y)*2+(self._z*self._y)*2+(self._z*self._x)*2

class Cube:
    def __init__(self, a):
        self._a = a

    def get_volume(self) -> float:
        return self._a*self._a*self._a

    def get_area(self) -> float:
        return (self._a*self._a)*6


class Ellipsoid:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    p = 1.6075

    def get_volume(self) -> float:
        return (4/3)*math.pi*self._y*self._z*self._x

    def get_area(self) -> float:
        return 4*math.pi*((((self._x**self.p)*(self._y**self.p))+((self._x**self.p)*(self._z**self.p))+((self._y**self.p)*(self._z**self.p)))/3)

class Cylinder:
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height

    def get_volume(self) -> float:
        return math.pi*self._radius*self._radius*self._height

    def get_area(self) -> float:
        return (2*math.pi*self._radius*self._height)+(math.pi*self._radius*self._radius)


if __name__ == '__main__':
    e = Ellipsoid(10, 20, 13)
    print(e.get_volume())
