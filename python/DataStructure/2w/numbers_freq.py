def solution(lst):
    freq = [0] * 256

    for i in lst:
        freq[i] += 1

    ret = []
    for i in range(len(freq)):
        if freq[i] == max(freq):
            ret.append(i)
    # ret = [i for i in range(len(freq)) if freq[i] == max(freq)]   #Using List comprehension
    if freq[ret[0]] == len(lst):        # 모든 element가 한가지 원소일 때
        return []
    elif len(ret) == len(lst):          # 모든 element가 다른 원소일 때
        return []
    else:
        return ret










print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([1, 1, 1, 1, 1, 1])) #[]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]