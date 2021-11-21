# 정답률이 높은 문제들로 이번에 구성하다 보니 다 쉬운 문제들이었다.
# 당황스럽네...
import sys


def invitation():
    N = int(input())
    time = list(map(int, sys.stdin.readline().split()))
    time.sort(reverse=True)
    answer = 0
    for i in range(N):
        answer = max(answer, i + 1 + time[i])
    return answer + 1


print(invitation())