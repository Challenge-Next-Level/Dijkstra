import sys
import heapq


def christ():
    n = int(sys.stdin.readline())
    heap = []
    for i in range(n):
        info = sys.stdin.readline()
        number = list(map(int, info.split()))
        if number[0] == 0:
            if len(heap) == 0:
                print(-1)
            else:
                answer = heapq.heappop(heap)
                print(-answer)
        else:
            for i in range(1, len(number)):
                heapq.heappush(heap, -number[i])
    return


christ()