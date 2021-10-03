import sys
import heapq


def combine_file():
    T = int(sys.stdin.readline())
    for i in range(T):
        chapter = int(sys.stdin.readline())
        cost = list(map(int, sys.stdin.readline().split()))
        heap = []
        for j in cost:
            heapq.heappush(heap, j)
        answer = 0
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            c = a + b
            heapq.heappush(heap, c)
            answer += c
        print(answer)

    return

combine_file()