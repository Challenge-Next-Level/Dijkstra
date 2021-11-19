# dfs, bfs 이런 것들을 복기하며 생각했지만 해결책이 떠오르지 않아 검색을 했다.
# kruskal 알고리즘이 딱인 해결법 이었고 비용이 작은 것부터 간선을 그냥 추가하면 되지 않을까 했지만
# 순환을 판단하는 방법을 따로 구현해야 해서 그냥 해결법대로 첫 출발 지점을 지정하고 하나씩 연결지으며
# 간선을 추가하는 방법을 카피했다.
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