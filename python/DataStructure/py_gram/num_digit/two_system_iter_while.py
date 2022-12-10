# import math
# BASE = 2
# num_dec = 11
# print(f"Decimal number = {num_dec}")
# cnt_iter = int(math.log(num_dec,2))
# num_bin = ""
#
# while cnt_iter > 0:
#     num_bin = str(num_dec % BASE) + num_bin
#     num_dec = num_dec // BASE
#     cnt_iter -= 1
#
# num_bin = str(num_dec) + num_bin
# print(f"Binary number = {num_bin}")

# cnt_iter 가 필요한가?

import math
BASE = 2
num_dec = 11
print(f"Decimal number = {num_dec}")
num_bin = ""

while num_dec >= BASE:
    num_bin = str(num_dec % BASE) + num_bin
    num_dec = num_dec // BASE

num_bin = str(num_dec) + num_bin
print(f"Binary number = {num_bin}")

# n진수에 맞게 나눗셈을 실시, cnt_iter가 아닌 BASE에 의존하여 나눗셈 횟수 결정

