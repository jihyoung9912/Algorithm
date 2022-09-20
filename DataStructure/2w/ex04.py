import math

num = 5923
sum_ = 0

exp = int(math.log10(num))

for i in range(exp, -1, -1):
    sum_ += num // 10 ** i
    num = num % 10 ** i

print(sum_)