# 작업이 걸리는 시간에 대해 heap으로 정렬하면 되는 문제
# 근데 내가 구현한거는 틀리는 문제. 개빡침. 런타임에러, 시간초과 하;;
import heapq


def solution(jobs):
    now, answer, index = 0, 0, 0
    start = -1
    to_do = []
    while index < len(jobs):
        # 현재 시간까지 들어올 수 있는 작업 모두 추가
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(to_do, [j[1], j[0]])
        if len(to_do) > 0:
            do = heapq.heappop(to_do)
            start = now
            now += do[0]
            answer += (now - do[1])
            index += 1
        else:
            now += 1

    return int(answer/len(jobs))


j = [[0, 3], [1, 9], [2, 6]]
print(solution(j))