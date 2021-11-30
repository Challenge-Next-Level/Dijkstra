# dfs, bfs 이런 것들을 복기하며 생각했지만 해결책이 떠오르지 않아 검색을 했다.
# 해결법에서 kruskal 얘기를 워낙해서 kruskal 알고리즘인줄! 알았다. (다른 문제를 풀면서 이게 kruskal이 아니란걸 깨달았다...)
# 오히려 prim과 더 가까운 해결법이었고 하지만 따져보면 정확한 prim algorithm 구현도 아니다.
# 아래 해결법은 하나의 정점을 선택 후 정점과 연결된 간선 중 가중치가 가장 낮은 것들을 선택하며 간선을 추가하는 형식이다.
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key=lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = {costs[0][0]}  # 출발 지점 초기 설정.
    # 1. 모든 지점이 routes에 추가될 때까지 반복
    while len(routes) != n:
        # 2. 간선을 하나씩 이어나간다.
        for i, cost in enumerate(costs):
            # 3. 순환을 만드는 간선은 피한다.
            if cost[0] in routes and cost[1] in routes:
                continue
            # 4. 실질적으로 간선을 추가하는 시점
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                # 추가된 간선을 단순히 삭제시키지 않는 이유는 위에서 반복문으로 costs를 사용하고 있기 때문
                # 그냥 간선을 의미 없게 변경 시킨다
                costs[i] = [-1, -1, -1]
                break
    return ans


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) #4
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])) #15
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])) #8