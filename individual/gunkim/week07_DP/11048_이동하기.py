# 나의 재귀 풀이보다 더 쉽게 2개의 for문을 통해 dp값을 알아내는 것이 더 좋은 방법이다(우, 하, 우하 탐색 밖에 안하기 때문에)
# 나는 재귀를 이용했는데 처음에 RecursionError가 발생해서 이유를 찾아보았다
# Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어져서 그렇다. sys.getrecursionlimit()로 값을 출력하면 1000이 출력된다
# 이 문제는 n, m이 1000까지 올 수 있어 충분히 최대 깊이보다 더 많이 깊어질 수 있었다. sys.setrecursionlimit(10**6)로 1,000,000으로 설정했다
# 앞서 말했듯이 재귀를 사용하지 않는 풀이가 가장 정석인 것 같다(왜냐면 n을 괜히 1000으로 둔게 아닌 것 같아서...)
import sys
sys.setrecursionlimit(10**6)


def solution():
    # n: 행, m: 렬
    n, m = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, sys.stdin.readline().split()))
    dp = [[-1] * m for _ in range(n)]

    def move(y, x):
        if y >= n or x >= m:
            return 0
        if y == n - 1 and x == m - 1:
            return arr[y][x]
        if dp[y][x] != -1:
            return dp[y][x]
        down = move(y + 1, x)
        right = move(y, x + 1)
        right_down = move(y + 1, x + 1)
        dp[y][x] = max(max(down, right), right_down) + arr[y][x]
        return dp[y][x]

    return move(0, 0)


print(solution())