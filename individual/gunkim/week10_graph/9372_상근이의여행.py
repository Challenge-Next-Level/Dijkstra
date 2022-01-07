import sys

T = int(input())
for _ in range(T): # 테스트 케이스 수 만큼 실행
    N, M = map(int, sys.stdin.readline().split()) # 국가의 수, 비행기 종류
    graph = [[] for _ in range(N + 1)] # 국가를 연결하는 경로 세팅
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    # 방문 여부를 통해 처음 이용하는 비행기인지 알 수 있음
    visit = [0] * (N + 1)

    def dfs(country, count): # 처음 방문하는 곳을 dfs 탐색
        visit[country] = 1 # 방문 표시
        for i in graph[country]:
            if visit[i] == 0:
                count = dfs(i, count + 1)
        return count
    print(dfs(1, 0))