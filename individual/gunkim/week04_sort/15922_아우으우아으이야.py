# 처음에 선분 하나하나와 비교를 하며 그곳에 선분이 겹치는지 판단해야 되는 건가 생각을 했다
# 하지만 너무 많은 반복을 해야할 것 같아서 시도를 하지 않았다
# 알고리즘 분류를 보았는데 스위핑이 있어서 '스위핑 알고리즘'을 찾아보았다
import sys
INF = 1000000000


def ah():
    N = int(input())
    answer = []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        answer.append(line)
    # 스위핑 알고리즘 사용을 위한 정렬
    answer.sort()
    left, right = -INF, -INF
    total = 0
    for i in range(N):
        # 선분이 기존 선분과 겹치지 않는 다면 기존 선분을 total에 더해주고 새로운 선분으로 업데이트
        if answer[i][0] > right:
            total += right - left
            left = answer[i][0]
            right = answer[i][1]
        # 겹친다면 조건에 따라 기존 선분을 업데이트
        elif answer[i][1] > right:
            right = answer[i][1]
    total += right - left
    print(total)
    return


ah()