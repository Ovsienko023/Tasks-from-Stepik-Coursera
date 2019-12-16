a = int(input())
b = int(input())
c = int(input())

if a < b:
    min = a
    if min > c:
        min = c           
else:
    min = b
    if min > c:
        min = c

if a < b:
    max = b
    if max < c:
        max = c
else:
    max = a
    if max < c:
        max = c 

s = ((a + b + c) - min) - max
 
print(min,'min')
print(max,'max')
print(s, 'среднее')
