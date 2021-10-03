import sys
import heapq
import math

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if heap :
            x = heapq.heappop(heap)
            print(math.floor(x[1]))
            # remember: elements with priority are stored as tuple,
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(n), n+0.5))
    
