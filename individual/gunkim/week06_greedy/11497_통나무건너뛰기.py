# 제일 큰 통나무를 기준으로 왼쪽, 오른쪽에 그 다음으로 큰 통나무를 세운다.
# 그렇게 세워지는 통나무들의 난이도를 계산한다.
# 이게 되네...? 예외가 있을 줄 알았는데...
import sys


def skipLog():
    T = int(input())
    for i in range(T):
        N = int(input())
        log = list(map(int, sys.stdin.readline().split()))
        log.sort(reverse=True)
        idx = 1
        left, right = log[0], log[0]
        answer = 0
        while idx < N:
            answer = max(answer, abs(left - log[idx]))
            left = log[idx]
            if idx + 1 < N:
                answer = max(answer, abs(right - log[idx + 1]))
                right = log[idx + 1]
            idx += 2
        print(answer)

    return


skipLog()