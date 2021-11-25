# 역시 dp 문제는 간단한 점화식을 빠르게 생각해내는 것이 중요한 것 같다.
# 이 문제는 dp[i] = max(dp[i - 1], dp[i - 2] + money[i]) 라는 점화식을 떠올리는게 우선이었다.
# 그리고 집은 링처럼 순환연결되어 있기 때문에 첫 집을 방문하냐 안하냐에 따라 구분하여 dp값을 계산해야 했다.
def solution(money):
    size = len(money)
    # 1. 첫 번째 집을 무조건 방문하는 경우 dp 계산
    dp1 = [0] * size
    dp1[0] = money[0]
    for i in range(1, size - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    # 2. 첫 번째 집을 방문하지 않는 경우 dp 계산
    dp2 = [0] * size
    for i in range(1, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    # 훔친 금액의 최댓값 반환
    return max(max(dp1), max(dp2))


m = [1, 2, 3, 1] # 4
print(solution(m))