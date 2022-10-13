def solution(lst):
    freq = [0] * 256
    for i in lst:
        freq[i] += 1    #lst의 인자를 i로 받고, i index에 빈도수를 더함

    ret = [i for i in range(len(freq)) if freq[i] == max(freq)] #i가 freq를 돌며 빈도수의 최대값을 가진 값을 뽑아옴
    if len(lst) == len(ret):
        return []
    return ret


print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]