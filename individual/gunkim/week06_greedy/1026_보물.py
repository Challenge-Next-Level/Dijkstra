# 이런 문제를 이전에 본 적이 있다. B를 재배열 불가라는 조건이 문제에 작성되어 있지만
# 답만 추출하면 돼서 사실 재배열 해도 상관없다. ㅎㅎ;;
import sys


def treasure():
    answer = 0
    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    A.sort()
    B.sort(reverse=True)
    for i in range(N):
        answer += A[i] * B[i]
    return answer


print(treasure())