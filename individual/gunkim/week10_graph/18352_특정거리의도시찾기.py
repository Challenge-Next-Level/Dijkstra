import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split()) # 도시의 수, 도로의 수, 거리 정보, 출발 도시 번호
road = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    road[a].append(b)
visit = [-1] * (N + 1) # 방문 도시, -1로 설정하는 이유: 거리가 0인 곳으로 설정되는 곳도 있다.


def bfs(node): # bfs 탐색을 하며 도시까지의 거리 계산
    dq = deque([node]) # 첫 시작 노드
    visit[node] = 0
    while dq:
        nxt = dq.popleft()
        for i in road[nxt]:
            if visit[i] == -1: # 방문하지 않았던 노드는 현재노드거리 + 1
                visit[i] = visit[nxt] + 1
                dq.append(i)


bfs(X) # X도시에서 bfs 탐색
for i in range(N + 1):  # 거리가 K인 곳을 출력
    if visit[i] == K:
        print(i)
if K not in visit: # K인 곳이 없다면 -1 출력
    print(-1)