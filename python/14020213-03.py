for number in range(999, 10000):
    digit_1 = number % 10
    digit_2 = number / 10 % 10
    digit_3 = number / 100 % 10
    digit_4 = number / 1000
    if(int(digit_4)**4) + (int(digit_1)**1) == (int(digit_2)**2) + (int(digit_3)**3):
        print(number)