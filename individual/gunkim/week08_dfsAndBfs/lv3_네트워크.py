def solution(n, computers):
    network = 0
    stack = []
    visit = []

    # 연결된 네트워크를 bfs 탐색
    def bfs(com):
        stack.append(com)
        while stack:
            num = stack.pop()
            visit.append(num)
            for j in range(n):
                if j != num and computers[num][j] == 1 and j not in visit:
                    stack.append(j)

    # 네트워크의 갯수를 카운트
    for i in range(n):
        # 연결된 네트워크는 bfs를 통해 탐색
        if i not in visit:
            bfs(i)
            network += 1
    return network


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1