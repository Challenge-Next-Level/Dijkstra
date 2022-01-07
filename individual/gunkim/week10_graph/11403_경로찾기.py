import sys

N = int(input())
graph = []
for _ in range(N): # 그래프 세팅
    graph.append(list(map(int, sys.stdin.readline().split())))
for start in range(N): # 각 지점에서 갈 수 있는 모든 곳을 탐색
    route = []
    for idx, go in enumerate(graph[start]): # start에서 갈 수 있는 지점을 route에 모두 추가
        if go == 1:
            route.append(idx)
    while route: # route에서 갈 수 있는 곳은 start에서도 갈 수 있음!
        end = route.pop()
        for idx, go in enumerate(graph[end]):
            if go == 1 and graph[start][idx] == 0:
                graph[start][idx] = 1
                route.append(idx)
for g in graph: # 출력
    print(' '.join(map(str, g)))