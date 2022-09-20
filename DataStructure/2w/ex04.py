import math

num = 5923
cnt_iter = int(math.log10(num))
sum_ = 0

while cnt_iter >= 0:
    sum_ += num // 10 ** cnt_iter
    num = num % 10 ** cnt_iter
    cnt_iter -= 1

print(sum_)
