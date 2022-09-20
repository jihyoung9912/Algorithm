import math

num = 5923
sum_ = 0

exp = int(math.log10(num))

for i in range(exp, -1, -1):
    x = num // 10 ** exp
    sum_ += x
    num -= x * 10 ** exp
    print(num)