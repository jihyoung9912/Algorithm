# num_bin = "1011"
# print(f"Binary number = {num_bin}")
#
# BIT = 3
# num_bin = num_bin[::-1]
# num_oct = []
# cnt = 0
#
# while cnt < len(num_bin):
#     cnt_, sum_ = 0, 0
#     while cnt_ < BIT:
#         if cnt >= len(num_bin):
#             break
#         sum_ += int(num_bin[cnt_]) * 2 ** cnt_
#         cnt += 1; cnt_ += 1
#     num_oct.append(sum_)
#
# num_oct = "".join(map(str, num_oct[::-1]))
# print(f"Octal number = {num_oct}")

# 오류의 개연성을 낮추기 위해

def convert_bin_to_octal(num_bin):
    BIT = 3
    num_oct = []
    octal = []

    while num_bin:
        cnt, sum_ = 0, 0
        while cnt < BIT and num_bin:
            octal.append(int(num_bin.pop()))
            cnt += 1
        sum_ = convert_octal(octal)
        num_oct.append(sum_)

    num_oct = "".join(map(str, num_oct[::-1]))
    print(f"Octal number = {num_oct}")


def convert_octal(grp):
    cnt, sum_ = 0, 0
    while grp:
        sum_ += int(grp.pop(0)) * 2 ** cnt      # pop reverse --> pop(0) 리스트에 요소가 있는지 조건을 추가하지 않아도 됨.
        cnt += 1
    return sum_


str_bin = "1011"
print(f"Binary number = {str_bin}")
convert_bin_to_octal(list(str_bin))