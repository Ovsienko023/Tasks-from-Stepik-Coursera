import math


def is_circle(x, y):
    rad = 1 / 2
    r_xy = math.sqrt(x**2 + y**2)
    if r_xy <= rad:
        return "Yes"
    else:
        return "No"


x, y = 1, 2
print(is_circle(x, y))
