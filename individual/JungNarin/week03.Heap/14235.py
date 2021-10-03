import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline()
    if a[0] == '0':
        if heap:
            print(heapq.heappop(heap) * -1)
        else:
            print(-1)
    else:
        a = list(map(int, a.split()))
        for i in a[1:]:
            heapq.heappush(heap, -1 * i)

        
