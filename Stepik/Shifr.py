lst_in = 'aaaccbbbn'
key = '#'
num = 1
lst_in = lst_in + key

for i in range(len(lst_in)):
    if lst_in[i] == key:
        break
    if lst_in[i] == lst_in[i+1]:
        num+=1        
    elif lst_in[i] != lst_in[i+1]:        
        print(lst_in[i],num)
        num = 1