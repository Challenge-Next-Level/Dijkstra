import heapq
import sys


def max_heap():
    N = input()
    heap = []
    for i in range(int(N)):
        num = int(sys.stdin.readline())
        if num == 0:
            if len(heap) == 0:
                print(0)
            else:
                answer = heapq.heappop(heap)
                print(-answer)
        else:
            heapq.heappush(heap, -num)
    return


max_heap()