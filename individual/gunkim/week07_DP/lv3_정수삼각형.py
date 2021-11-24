# 앞에서 푼 'N으로 표현'이란 문제보다는 훨씬 쉽다. 한 번에 통과했다!
def solution(triangle):
    # 해당 구간에서의 최적의 값을 저장할 dp를 생성 (구조는 triangle과 같음)
    dp = [[-1] * len(triangle[i]) for i in range(len(triangle))]

    def dfs(floor, idx):
        # 범위를 벗어나는 floor or idx 값이라면 0 리턴
        if floor >= len(triangle) or idx >= len(triangle[floor]):
            return 0
        # 이미 계산을 한 적 있다면 그 값 리턴
        if dp[floor][idx] != -1:
            return dp[floor][idx]
        # 왼쪽, 오른쪽으로 경로를 설정하여 최적의 값 탐색
        left = dfs(floor + 1, idx)
        right = dfs(floor + 1, idx + 1)
        dp[floor][idx] = max(left, right) + triangle[floor][idx]
        return dp[floor][idx]

    dfs(0, 0)
    return dp[0][0]


t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t)) # 30