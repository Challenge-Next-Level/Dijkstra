import sys
import heapq

N, M = sys.stdin.readline().split(" ")
N = int(N)
M = int(M)

cards = sys.stdin.readline().split(" ")
heap = []

for i in range(N):
    heapq.heappush(heap, int(cards[i]))
    
for i in range(M):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    heapq.heappush(heap, first + second)
    heapq.heappush(heap, first + second)

print(sum(heap))


