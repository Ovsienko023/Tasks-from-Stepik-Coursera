d = dict()
d = {i:chr(i) for i in range(65, 65 + 26)}


for key in sorted(d, reverse=True):
    print(key)
