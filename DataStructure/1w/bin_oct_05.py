def convert_bin_to_octal(num_bin):
    BIT = 3
    num_oct = []    #최종 8진수 값 저장소
    octal = []      #임시 3개 8진수 값 저장소

    while num_bin:  #num_bin을 pop으로 제거 예정. num_bin이 존재할 동안 반복 진행
        cnt, sum_ = 0, 0
        while cnt < BIT and num_bin: #3회씩 끊어서 반복 + num_bin 존재할 동안
            octal.append(int(num_bin.pop())) #임시 list octal에 3개 값씩 pop이기에 역순으로
            cnt += 1
        cnt = 0
        while octal: #octal이 존재할 동안
            bin_ = octal.pop(0) #bin_변수에 첫 index값부터 할당 시작
            sum_ += 2**cnt * bin_
            cnt += 1
        num_oct.append(sum_)

    num_oct = "".join(map(str, num_oct[::-1]))
    print(f"Octal number = {num_oct}")

str_bin = "1011"
print(f"Binary number = {str_bin}")
convert_bin_to_octal(list(str_bin))