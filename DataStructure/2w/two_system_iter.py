import math

BASE = 2
num_dec = 11
num_bin = ""
print(f"Decimal number = {num_dec}")

cnt_iter = int(math.log(num_dec, 2))

while cnt_iter > 0:
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin
    cnt_iter -= 1


num_bin = str(num_dec) + num_bin

print(f"Binary number = {num_bin}")