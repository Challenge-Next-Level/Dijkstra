import heapq
import sys

heap = []
N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)
