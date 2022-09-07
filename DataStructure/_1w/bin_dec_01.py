# num_bin = '1011'
# print(f"Binary number = {num_bin}")
#
# num_dec = 0
#
# for i in range(0, len(num_bin)):
#     num_dec += int(num_bin[len(num_bin) - i - 1]) * 2 ** i
#
# print(f"decimal number = {num_dec}")

# num_bin = '1011'
#
# exp = 0
# num_dec = 0
#
# cnt_iter = len(num_bin)
# while cnt_iter > 0:
#     num_dec += 2**exp * int(num_bin[cnt_iter - 1])
#     exp += 1
#     cnt_iter -= 1
#
# print(num_dec)