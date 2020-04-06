


def find(lst, num):
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1
    lst = sorted(lst)

    while lst[mid] != num and low <= high:
        if num > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    
    if low > high:
        return 'Not num'
    else:
        return mid

print(find([2,8,4,5,6,2,5], 2))

