import math

BASE = 2
num_dec = 54
print(f"Decimal number = {num_dec}")
cnt_iter = int(math.log(num_dec,2))
num_bin = ""

while cnt_iter > 0:
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin
    cnt_iter -= 1

num_bin = str(num_dec) + num_bin
print(f"Binary number = {num_bin}")

# log로 나눗셈 횟수를 정하여 진행, num_dec // BASE의 결과 값의 r을 뽑지 않게 주의

