num = 5923
sum_ = 0

while num != 0:
    sum_ += num % 10
    num = num // 10

print(sum_)


#계산할 때마다 뭔가 변경되는 값, 초기화 되는 값을 종료 조건으로 두는 경우가 많다. 