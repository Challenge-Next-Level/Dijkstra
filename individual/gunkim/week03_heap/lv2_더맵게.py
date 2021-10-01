import heapq


def solution(scoville, K):
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    answer = 0
    while True:
        if len(h) == 1:
            if h[0] < K:
                return -1
            else:
                return answer
        if h[0] >= K:
            return answer
        else:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            num = a + b * 2
            heapq.heappush(h, num)
            answer += 1


s = [1, 2, 3, 9, 10, 12]
k = 7
solution(s, k)
