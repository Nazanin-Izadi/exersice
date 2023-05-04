number = int(input("please enter the value : "))
nr = 0
nr_5000 = number / 5000
nr_2000 = number / 2000
nr_1000 = number / 1000
for i in range(1, int(nr_5000)+1):
    for j in range(1, int(nr_2000)+1):
        for k in range(1, int(nr_1000)+1):
            if 5000*i + 2000*j + 1000*k == number:
                nr+=1
print(nr)