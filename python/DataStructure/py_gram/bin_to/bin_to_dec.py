# Bin to Dec

num_bin = "1011"
print(f"Binary number = {num_bin}")     # bin is 1011

exp = 0
num_dec = 0
# len_ = len(num_bin) - 1
#
# while len_ >= 0:
#     num_dec += int(num_bin[len_]) * 2 ** exp
#     exp += 1; len_ -= 1

# I have to make two variables to make Dec
# So, Reverse bin num to make only one variable

# num_bin = num_bin[::-1]
#
# while exp < len_ + 1:
#     num_dec += int(num_bin[exp]) * 2 ** exp
#     exp += 1
#

# Using DataStructure

num_bin = list(num_bin)

while num_bin:
    num_dec += int(num_bin.pop()) * 2 ** exp
    exp += 1

print(f"Decimal number = {num_dec}")