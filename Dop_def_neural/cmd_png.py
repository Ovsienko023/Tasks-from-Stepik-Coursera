def cmd_png():
    with open("Tren_csv\\mnist_train.csv") as f:
        tren = f.readline()
        tren_1 = f.readline()
    tren_1 = tren_1[1:].split(",")
    tren_1.remove(tren_1[0]) 

    n = 0

    #print(tren_1)
    tren_1 = list(tren_1)

    fin = tren_1


    for i in range(len(tren_1)):
        if tren_1[i] != '0':
            tren_1[i] = "*"



    for i in range(len(tren_1)):
        n += 1
        if n == 28:
            tren_1[i] = tren_1[i] + '\n'
            n = 0


    tren_1_str = ''.join(tren_1)

    with open('test_png.txt', 'w') as w:
        w.write(tren_1_str)
