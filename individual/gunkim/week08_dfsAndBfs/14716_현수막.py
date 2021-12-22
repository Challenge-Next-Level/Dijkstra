# dfs를 재귀를 이용한 풀이를 사용했는데 재귀 깊이 제한으로 인한 recursion error가 발생
# bfs로 전환하여 dequeue를 활용한 풀이를 사용했다
# 그리고 방향 리스트를 하나 만들어 사용한 것이 클린 코드에 도움을 줌
from collections import deque
N, M = list(map(int, input().split()))
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))
visit = [[0] * M for _ in range(N)]
# 방향: 좌상/상/우상/좌/우/좌하/하/우하
d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    visit[y][x] = 1
    while q:
        qy, qx = q.popleft()
        for i in d:
            ny = qy + i[0]
            nx = qx + i[1]
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1 and paper[ny][nx] == 1 and visit[ny][nx] == 0:
                q.append([ny, nx])
                visit[ny][nx] = 1


answer = 0
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1 and visit[i][j] == 0:
            answer += 1
            bfs(i, j)
print(answer)