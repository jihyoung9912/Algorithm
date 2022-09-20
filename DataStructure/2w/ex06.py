def solution(lst):
    freq = [0] * 256
    for i in lst:
        freq[i] += 1    #lst의 인자를 i로 받고, i index에 빈도수를 더함

    ret = [i for i in range(len(freq)) if freq[i] == max(freq)]
    if len(lst) == len(ret):
        return []
    return ret


print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([1, 2, 3, 4, 5, 6])) #[5]