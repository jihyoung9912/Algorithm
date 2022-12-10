BASE = 2
num_dec = 11
print(f"Decimal number = {num_dec}")

num_bin = ''

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_dec, r = num_dec // BASE, num_dec % BASE
num_bin = str(r) + num_bin

num_bin = str(num_dec) + num_bin
print(num_bin)