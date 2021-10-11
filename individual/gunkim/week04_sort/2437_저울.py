# 수학적인 생각이 좋아야 하는 문제. 나에겐 너무 어려웠다
import sys


def scale():
    N = int(input())
    weight = list(map(int, sys.stdin.readline().split()))
    weight = sorted(weight)
    num = 1
    for i in range(N):
        if num < weight[i]:
            break
        num += weight[i]
    print(num)
    return


scale()