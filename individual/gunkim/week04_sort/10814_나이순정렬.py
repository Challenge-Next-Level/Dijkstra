# sort와 sorted는 stable한 정렬이다
import sys


def age_sort():
    N = int(input())
    answer = []
    for i in range(N):
        person = sys.stdin.readline().split()
        answer.append(person)
    # 나이를 비교해야 하니 int형으로 변환
    ans = sorted(answer, key=lambda x: int(x[0]))
    for i in ans:
        print(' '.join(i))
    return


age_sort()