def division_by_zero(num):
    try:
        answer = num / 0
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")

division_by_zero(7)