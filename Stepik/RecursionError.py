def rec(x):
    try:
        print(x)
        x += 1
    
        rec(x)
    except RecursionError:
        rec(x)

rec(1)
