import sys


def solution():
    N = int(input())
    dict = {}
    for i in range(N):
        dict[i + 1] = set()
    connect = int(input())
    for i in range(connect):
        a, b = map(int, sys.stdin.readline().split())
        dict[a].add(b)
        dict[b].add(a)

    visit = []

    def bfs(node):
        stack = [node]
        while stack:
            for j in dict[stack.pop()]:
                if j not in visit:
                    stack.append(j)
                    visit.append(j)
    bfs(1)
    return len(visit) - 1


print(solution())