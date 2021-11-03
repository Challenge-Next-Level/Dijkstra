# 처음 날짜부터 최대로 벌 수 있는 돈을 계산하며 머리를 굴렸었다.
# 하지만 좋은 규칙은 발견할 수 없었고 결국 다른 분의 풀이를 보고 깨달았다.
# 마지막 날짜부터 역순으로 계산을 해야했던 것이다. dp가 보통 이런식의 풀이법이 많은데 새까맣게 잊고 있었다.
import sys


def leave():
    N = int(input())
    T, P = [], []

    # 벌 수 있는 금액의 최댓값을 담는다. 날짜의 역순으로 채워나간다.
    # dp[i] = dp[i + 1] 개념을 사용하기 위해 기존 index크기보다 하나 크게 생성했다.
    dp = [0] * (N + 1)

    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        T.append(a)
        P.append(b)

    for i in range(N - 1, -1, -1):
        # 현재 날짜 + 상담 필요 날짜 > 총 기간
        if T[i] + i > N:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])

    # 맨 처음 날짜의 dp값이 최댓값을 보유함
    return dp[0]


print(leave())