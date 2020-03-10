import csv
import re


lst = list()
with open("crimes.csv") as crim:
    crimes = csv.reader(crim)
    for i in crimes:
        lst.append(i)


prim = lst[0].index('Primary Type')
date = lst[0].index('Date')
prymary_lst = list()
for i in range(1, len(lst)):
    # print(lst[i][prim])
    # print(lst[i][date])
    match = re.search('2015', lst[i][date])
    if match:
        prymary_lst.append(lst[i][prim])


num = 0
for i in prymary_lst:
    fin = prymary_lst.count(i)
    if fin > num:
        num = fin
        prym_max = i
    else:
        continue
print(prym_max, num)
