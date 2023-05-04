import math
n = int(input("please enter n :"))
x = int(input("please enter x as the corner : "))
a = 1
sum = 0
for n in range(1, n+1, 2):
    p = math.pow(x, n)
    q = math.factorial(n)
    sum = sum + (p/q) * a
    a = -a
print("sin (",x,") is : ", float(sum))