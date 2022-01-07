from collections import deque


def dfs(node, visit, adjNode): # dequeue를 이용한 dfs 탐색
    dq = deque([[node, 0]])
    while dq:
        node, count = dq.popleft()
        if visit[node] == -1:
            visit[node] = count # dq가 갖고 있는 count값이 1에서 node까지 거리임
            count += 1 # 뒤에 추가할 node는 거리를 1증가 시켜야함
            for i in adjNode[node]:
                if visit[i] == -1:
                    dq.append([i, count])


def solution(n, edge):
    adjNode = [[] for _ in range(n + 1)] # 인접 노드
    visit = [-1] * (n + 1) # 방문 체크 및 거리 값으로도 활용
    for i in edge: # 인접 노드 세팅
        a, b = i
        adjNode[a].append(b)
        adjNode[b].append(a)
    dfs(1, visit, adjNode) # 1에서 dfs 탐색
    distance = max(visit) # 가장 거리가 먼 곳
    return visit.count(distance)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))