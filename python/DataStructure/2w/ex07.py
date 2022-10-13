def solution(lst):
    freq = {x:lst.count(x) for x in set(lst)} #{1: 1, 2: 1, 3: 1, 4: 1, 5: 2}
    if len(freq) == 1 or len(freq) == len(lst):
        return []
    return [x for x in freq if freq[x] == max(freq.values())]


print(solution([1, 2, 3, 4, 5, 5])) #[5]