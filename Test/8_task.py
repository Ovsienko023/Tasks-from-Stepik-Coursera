





class Figure():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Figure):
    name = 'square'

    def __init__(self, length, width):
        super().__init__(length, width)

    def get_area(self):
        return self.length * self.length




lst = [Square(5, 6)]

def area(lst):
    for obj in lst:
        if obj.name == 'square':
            fin = obj.get_area()
    return fin

print(area(lst))