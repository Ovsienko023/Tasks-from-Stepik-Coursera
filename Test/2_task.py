lst = [1, 4, 6, 8, 0, 6, 10, 3]


def max_(list_num):
    max = 0
    for num in list_num:
        if num > max:
            max = num
    return max

print(max_(lst))
