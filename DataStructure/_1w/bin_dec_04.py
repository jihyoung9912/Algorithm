num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
num_bin = list(num_bin)
cnt_iter = 0

while num_bin:
    num_dec += 2 ** cnt_iter * int(num_bin.pop())
    cnt_iter += 1

print(f"Decimal number = {num_dec}")