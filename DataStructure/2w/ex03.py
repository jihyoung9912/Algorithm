BASE = 2
num_dec = 13
num_bin = ''
print(f"Decimal number = {num_dec}")


while num_dec >= BASE:
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin

num_bin = str(num_dec) + num_bin
print(f"Binary number = {num_bin}")