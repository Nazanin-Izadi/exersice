def count(number, digit):
    count = 0
    while(number > 0):
        if(number % 10 == digit):
            count = count + 1
        number = number // 10
    return count
number = int(input("please enter your number : "))
digit = int(input("please enter your digit : "))
print(count(number, digit))