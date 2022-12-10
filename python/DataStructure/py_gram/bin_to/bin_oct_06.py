def convert_octal(grp):
    cnt, sum_ = 0, 0
    while grp:
        bin_ = grp.pop(0)
        sum_ = 2 ** cnt * bin_
        cnt += 1
    return sum_

def convert_bin_to_octal(num_bin):
    BIT = 3
    num_oct = []
    octal = []

    while num_bin:
        cnt, sum_ = 0, 0
        while num_bin and cnt < BIT:
            octal.append(int(num_bin.pop()))
            cnt += 1

        sum_ = convert_octal(octal)
        num_oct.append(sum_)
    num_oct = ''.join(map(str, num_oct[::-1]))
    print(num_oct)

str_bin = "1011"
print(f"Binary number = {str_bin}")
convert_bin_to_octal(list(str_bin))
