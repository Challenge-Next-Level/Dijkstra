# for문을 하나만 사용하여 해결했다. 문제는 쉬움.
import sys


def ATM():
    answer = 0
    N = int(input())
    time = list(map(int, sys.stdin.readline().split()))
    time.sort()
    for i in range(N):
        answer += time[i] * (N - i)

    return answer


print(ATM())