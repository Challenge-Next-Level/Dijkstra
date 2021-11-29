# 풀었던 문제인데 도대체 왜 못풀었을까... 진짜 바보같다
# i번째 타일의 경우를 구하고 싶을 때 i-1번째에서 세로 타일을 붙이는 경우와 i-2번째에서 가로타일2개/정사각형1개 를 붙이는 경우를 더하면 된다
# 따라서 dp[i] = dp[i - 1] + (2 * dp[i - 2]) 라는 점화식이 완성된다
def solution():
    n = int(input())
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 1
    dp[1] = 3
    MOD = 10007
    for i in range(2, n):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD
    return dp[n - 1]


print(solution())