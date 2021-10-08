def solution(citations):
    answer = 0
    m = max(citations)
    s = sorted(citations, reverse=True)
    for i in range(m):
        h_max, h_min = 0, 0
        for j in s:
            if j >= i:
                h_max += 1
            elif j <= i:
                h_min += 1
        if h_max >= i and h_min <= i and answer < i:
            answer = i

    return answer


c = [3, 0, 6, 1, 5]
print(solution(c))