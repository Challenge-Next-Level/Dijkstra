# 진짜 어려운 문제다. 이유는 한 번에 dp값을 만들 수가 없기 때문
# 그래서 규칙성을 발견할 수가 없었다(물론 있지만) 입력되는 동전의 종류가 다른데 어떻게 점화식을 만들 수 있지? 란 생각을 했다
# 동전 종류 마다 dp에 경우의 수를 추가하는 식으로 만들어야 한다. 결국 dp 값은 for문 동안 끊임없이 수정된다
import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    coin = [0] * n
    for i in range(n):
        coin[i] = int(sys.stdin.readline().split()[0])
    coin.sort()
    dp = [0] * (k + 1)
    # 아래 숫자는 동전 1개를 이용하여 원하는 숫자를 만드는 경우를 추가하기 위한 초기화이다
    dp[0] = 1

    # 1. 값이 작은 동전부터 dp 값에 경우의 수를 넣어준다
    for c in coin:
        # 2. (1 ~ k)개 까지 차곡차곡 경우의 수를 추가한다
        for i in range(1, k + 1):
            if i - c >= 0:
                dp[i] += dp[i - c]
    return dp[k]


print(solution())