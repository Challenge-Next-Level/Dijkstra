import math


def solution():
    T = int(input())
    for i in range(T):
        site = list(map(int, input().split()))
        # 서, 동 쪽 사이트 갯수가 같다면 1
        if site[0] == site[1]:
            print(1)
        # 다르다면 Combination(동, 서)를 계산
        # nCk = n! / ((n - k)! * k!)
        else:
            print(math.factorial(site[1]) // (math.factorial(site[1] - site[0]) * math.factorial(site[0])))

    return


solution()