s = input()
a = input()
b = input()
num = 0

while s.count(a):
    s = s.replace(a, b)
    num += 1
    if num >= 1000:
        print("Impossible")
        break

if s.count(a) == 0 and num < 1000:
    print(num)
