from collections import Counter


def movie_director():
    answer = 666
    number = 1
    num = int(input())
    if num == 1:
        return answer
    while number < num:
        answer += 1
        lst = list(str(answer))
        c = Counter(lst)
        if c['6'] and c['6'] >= 3:
            cnt, seq = 0, 0
            for n in lst:
                if n == '6':
                    seq = 1
                    cnt += 1
                elif n != '6' and seq == 1:
                    seq = 0
                    cnt = 0
                if cnt == 3:
                    number += 1
                    break
    return answer


print(movie_director())