from collections import deque
M, N, K = list(map(int, input().split()))
paper, visit = [[0] * N for _ in range(M)], [[0] * N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for a in range(y1, y2):
        for b in range(x1, x2):
            paper[a][b] = 1
            visit[a][b] = 1
width = []
# 방향 설정을 도와주는 리스트: 동, 서, 남, 북
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(y, x):
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    # 한 칸씩 q에 저장할 때 마다 넓이를 1씩 늘려준다
    w = 1
    while q:
        qy, qx = q.popleft()
        for i in d:
            ny = qy + i[0]
            nx = qx + i[1]
            if 0 <= ny <= M - 1 and 0 <= nx <= N - 1 and paper[ny][nx] == 0 and visit[ny][nx] == 0:
                q.append([ny, nx])
                visit[ny][nx] = 1
                w += 1
    return w


for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and visit[i][j] == 0:
            width.append(bfs(i, j))
print(len(width))
# 숫자 리스트를 str 리스트로 형 변환 후 공백을 넣어 합쳐준다
print(' '.join(map(str, sorted(width))))