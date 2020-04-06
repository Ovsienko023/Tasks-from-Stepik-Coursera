import numpy

a = [[2 for j in range(2)] for i in range(2)]
b = [[4 for j in range(2)] for i in range(2)]


def multi_matr(a, b):
    a = numpy.array(a)
    b = numpy.array(b)
    return a.dot(b)

print(multi_matr(a, b))
