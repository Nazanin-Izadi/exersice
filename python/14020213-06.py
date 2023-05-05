umber = int(input("please enter a number between 1 and 80 : "))
for i in range(number):
    for j in range(number):
        if(i == 0 or i == number-1 or j == 0 or j == number-1):
            print("*", end=" ")
        elif(i == i and j == number-(i+1) or j == j and i == number-(j+1)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()