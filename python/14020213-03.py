# q1
# def count(number, digit):
#     count = 0
#     while(number > 0):
#         if(number % 10 == digit):
#             count = count + 1
#         number = number // 10
#     return count
# number = int(input("please enter your number : "))
# digit = int(input("please enter your digit : "))
# print(count(number, digit))
# q2
# import math
# n = int(input("please enter n :"))
# x = int(input("please enter x as the corner : "))
# a = 1
# sum = 0
# for n in range(1, n+1, 2):
#     p = math.pow(x, n)
#     q = math.factorial(n)
#     sum = sum + (p/q) * a
#     a = -a
# print("sin (",x,") is : ", float(sum))
# q3
# for number in range(999, 10000):
#     digit_1 = number % 10
#     digit_2 = number / 10 % 10
#     digit_3 = number / 100 % 10
#     digit_4 = number / 1000
#     if(int(digit_4)**4) + (int(digit_1)**1) == (int(digit_2)**2) + (int(digit_3)**3):
#         print(number)
# q4
# word = str()
# words = []
# while True:
#     word = input("please enter word : ")
#     if len(word) != 0:
#         words.append(word)
#     else:
#         break
# words.sort()
# print(words[-1])
# q5
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
# 6
# number = int(input("please enter a number between 1 and 80 : "))
# for number in range(1, number+1):
#     print("*")



