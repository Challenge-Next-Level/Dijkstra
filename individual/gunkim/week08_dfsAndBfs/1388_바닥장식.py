N, M = list(map(int, input().split()))
floor = []
for i in range(N):
    floor.append(input())
visit = [[0] * M for _ in range(N)]


def dfs(y, x):
    visit[y][x] = 1
    if x < M - 1 and floor[y][x] == '-' and floor[y][x + 1] == '-':
        dfs(y, x + 1)
    if y < N - 1 and floor[y][x] == '|' and floor[y + 1][x] == '|':
        dfs(y + 1, x)


answer = 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            answer += 1
            dfs(i, j)
print(answer)