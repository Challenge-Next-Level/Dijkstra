# 처음엔 bfs로 탐색하는 코드를 작성했는데 정확도 테스트도 통과하지 못했다
# 우향, 하향 진행만 하기 때문에 2중 for문을 사용하는 간단한 탐색 문제였다
def solution(m, n, puddles):
    # *유의*
    # 효율성 테스트에서 모듈로 나눠주지 않으면 통과하지 못한다
    # map의 크기는 최대 100 * 100 사이즈가 될 수 있으니 중간 경로들을 더한 값이 int의 범위를 충분히 넘을 수 있다
    # 하지만 python의 경우 long 형으로 계산시 문제가 없으며 마지막 리턴 때만 모듈로 나눠주면 된다
    MOD = 1000000007

    # 지도 생성 후 우물 표시 (배열과 x, y 좌표는 반대로 생각해야 한다)
    map = [[0] * m for _ in range(n)]
    for i in range(len(puddles)):
        map[puddles[i][1] - 1][puddles[i][0] - 1] = 1
    # dp 생성
    dp = [[0] * m for _ in range(n)]

    # 우향, 하향으로만 진행하기 때문에 2중 for문을 통해 좌, 상 dp 값들을 더하면 된다
    for y in range(n):
        for x in range(m):
            if x == 0 and y == 0:
                dp[y][x] = 1
            elif map[y][x] == 1:
                dp[y][x] = 0 # 우물로 오는 경우는 0으로 설정
            elif y == 0:
                dp[y][x] = dp[y][x - 1]
            elif x == 0:
                dp[y][x] = dp[y - 1][x]
            else:
                dp[y][x] = (dp[y][x - 1] + dp[y - 1][x]) % MOD

    return dp[n - 1][m - 1]


print(solution(100, 100, [])) # 690285631