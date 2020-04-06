import math

pi = math.pi

class Figure():
    names = ['square', 'circle', 'triangle']

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Figure):
    name = 'square'

    def __init__(self, length, width):
        super().__init__(length, width)

    def get_area(self):
        return self.length * self.length


class Circle(Figure):
    name = 'circle'

    def __init__(self, rad):
        self.rad = rad

    def get_area(self):
        return pi * (self.rad ** 2)



class Triangle(Figure):
    name = 'triangle'

    def __init__(self, length, width, c):
        self.c = c
        super().__init__(length, width)

    def get_area(self):
        p = (self.length + self.width + self.c) / 2
        s = math.sqrt(p*(p-self.length)*(p-self.width)*(p-self.c))
        return s


lst = [Square(5, 6), Circle(5), Triangle(3, 5, 6)]

def area(lst):
    for obj in lst:
        if obj.name in obj.names:
            fin = obj.get_area()
            print(fin)





    
    
print(area(lst))