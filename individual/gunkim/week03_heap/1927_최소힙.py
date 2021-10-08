# 시간 제한으로 효율성이 중요했는데 구현상으로는 문제가 없었지만
# 역시나 input이 sys.stdin보다 좋지 않은 성능을 보여 수정이 필요했다
import heapq
import sys


def min_heap():
    N = input()
    heap = []
    for i in range(int(N)):
        num = int(sys.stdin.readline())
        if num == 0:
            if heap:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, num)
    return


min_heap()