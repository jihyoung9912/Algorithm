# 자릿수 합 구하기 Using for loop
import math

num = 5923
sum_ = 0
exp = int(math.log10(num))

# for i in range(exp, -1, -1):
#     sum_ += num // 10 ** i
#     num = num % 10 ** i
#
# print(sum_)

# 자릿수 합 구하기 Using while loop
# 10으로 나눈 몫과 나머지를 이용하여 num != 0으로 종료 조건 설정

while num != 0:
    sum_ += num % 10
    num = num // 10

print(sum_)

